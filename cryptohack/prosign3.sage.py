

# This file was *autogenerated* from the file prosign3.sage
from sage.all_cmdline import *   # import sage library

_sage_const_13381 = Integer(13381); _sage_const_0xfffffffffffffffffffffffffffffffeffffffffffffffff = Integer(0xfffffffffffffffffffffffffffffffeffffffffffffffff); _sage_const_0xfffffffffffffffffffffffffffffffefffffffffffffffc = Integer(0xfffffffffffffffffffffffffffffffefffffffffffffffc); _sage_const_0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1 = Integer(0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1); _sage_const_0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012 = Integer(0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012); _sage_const_0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811 = Integer(0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811); _sage_const_0xffffffffffffffffffffffff99def836146bc9b1b4d22831 = Integer(0xffffffffffffffffffffffff99def836146bc9b1b4d22831); _sage_const_60 = Integer(60); _sage_const_1 = Integer(1); _sage_const_16 = Integer(16); _sage_const_0 = Integer(0)
from pwn import * 
from json import dumps, loads 
from hashlib import sha1
from Crypto.Util.number import bytes_to_long 
context.log_level = 'debug'
sock = remote('socket.cryptohack.org', int(_sage_const_13381 ))
sock.recvline()
def send(**kwargs):
    #print('send', kwargs)
    sock.sendline(dumps(kwargs))
def get():
    msg = loads(sock.recvline())
    #print('recv', msg)
    return msg 

E = EllipticCurve(GF(_sage_const_0xfffffffffffffffffffffffffffffffeffffffffffffffff ), [_sage_const_0xfffffffffffffffffffffffffffffffefffffffffffffffc , _sage_const_0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1 ])
G = E((_sage_const_0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012 , _sage_const_0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811 ))
n = E.order()
assert n == _sage_const_0xffffffffffffffffffffffff99def836146bc9b1b4d22831 
f = GF(n)

send(option='sign_time')
orig_msg = get() 
max_k = _sage_const_60  #int(orig_msg['msg'].split(':')[1])
h = bytes_to_long(sha1(orig_msg['msg'].encode()).digest())
for i in range(_sage_const_1 , max_k):
    k = f(i)
    r = f(int(orig_msg['r'], _sage_const_16 ))
    s = f(int(orig_msg['s'], _sage_const_16 ))
    #print(type(s),type(k),type(f(h)),type(r), type(r^-1))
    privKey = ((s*k)-f(h))*r**-_sage_const_1 
    new_h = bytes_to_long(sha1(b'unlock').digest())
    R = int(k)*G 
    r = R[_sage_const_0 ]
    s = k**-_sage_const_1  * (f(new_h) + f(r)*privKey)
    send(option='verify', msg='unlock', r=hex(int(r)), s=hex(int(s)))
    msg = get()
    #print('res', msg)
    if 'flag' in msg:
        print(msg)
        break

