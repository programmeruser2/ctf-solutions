from ctypes import CDLL 
from pwn import *
from z3 import *
libc = CDLL('libc.so.6')
contents = open('simpleencryptor_flag.enc', 'rb').read()
seed, ct = contents[:4], contents[4:]
assert len(seed) + len(ct) == len(contents)
seed = u32(seed)
libc.srand(seed)
s = Solver()
svars = []
for i, c in enumerate(ct):
    dec = BitVec(f'dec{i}', 8)
    svars.append(dec)
    t1 = dec^libc.rand()
    shift_amt = libc.rand()&7 
    t2 = RotateLeft(t1, shift_amt)
    s.add(t2 == c)
assert s.check() == sat
flag = b''
model = s.model()
for i in range(len(ct)):
    flag += bytes([model[svars[i]].as_long()])
print(flag)

