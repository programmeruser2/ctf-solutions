from web3 import Web3
from web3.middleware import geth_poa_middleware
host = 'https://blockchain-eightfivefourfive-3d309037bff622e8-eth.2023.ductf.dev:8545'
w3 = Web3(Web3.HTTPProvider(host))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

