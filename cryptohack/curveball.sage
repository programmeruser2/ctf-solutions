from json import dumps 
from pwn import * 
r = remote('socket.cryptohack.org', int(13382))
def send(**kwargs):
    r.sendline(dumps(kwargs).encode())
p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b 
E = EllipticCurve(GF(p), [a,b])
ring = Integers(E.order())
host = 'www.bing.com'
d = 2 
curve = 'secp256r1'
pubkey = E((0x3B827FF5E8EA151E6E51F8D0ABF08D90F571914A595891F9998A5BD49DFA3531, 0xAB61705C502CA0F7AA127DEC096B2BBDC9BD3B4281808B3740C320810888592A))
g = pubkey*int(ring(d)^-1)
send(private_key = int(d), host = host, curve = curve, generator = [int(g[0]), int(g[1])])
r.interactive()

