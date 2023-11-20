from pwn import * 
from json import dumps, loads
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad 

def bxor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))
context.log_level = 'debug'
r = remote('socket.cryptohack.org', 13388)
#r = process(['python3', 'md0_challenge.py'])
def rl():
    return loads(r.recvline().decode())
def sl(d):
    r.sendline(dumps(d).encode())
r.recvline()
sl({'option': 'sign', 'message': b'\x00'.hex()})
data = rl()
signature = bytes.fromhex(data['signature'])
realdata = b'admin=True'
sigdata = pad(realdata, 16)
newsig = bxor(AES.new(sigdata, AES.MODE_ECB).encrypt(signature), signature)
sl({'option': 'get_flag', 'signature': newsig.hex(), 'message': (pad(b'\x00',16)+realdata).hex()})
r.interactive()


