from Crypto.Util.number import bytes_to_long, long_to_bytes
from z3 import *
ct = b'\x62\x56\x06\x30\x50\x69\x51\x21\x18\x74\x27\x62\x50\x7e\x25\x11'
assert(len(ct) == 16)
ct = int.from_bytes(ct, 'little')
print(ct, hex(ct))
poly = ''
for i in range(127, -1, -1):
    if (ct>>i) & 1:
        poly += f'{"+" if len(poly) > 0 else ""}x^{i}'
print(poly)
"""s = Solver()
bits = 16 * 8
x = BitVec('x', bits)
mul_res = 0 
for i in range(0, bits):
    mul_res = If(Extract(i,i,x)==1, mul_res ^ (x<<i), mul_res)
s.add(mul_res == ct)
assert(s.check() == sat)
print(s.model())"""
#poly = 'x^57 + x^56 + x^53 + x^52 + x^51 + x^47 + x^41 + x^35 + x^34 + x^32 + x^31 + x^28 + x^27 + x^26 + x^24 + x^23 + x^21 + x^20 + x^19 + x^18 + x^15 + x^14 + x^13 + x^10 + x^9 + x^8 + x^7 + x^1'
#poly = 'x^53 + x^51 + x^50 + x^48 + x^46 + x^45 + x^44 + x^43 + x^42 + x^40 + x^39 + x^38 + x^36 + x^35 + x^32 + x^29 + x^28 + x^27 + x^24 + x^19 + x^18 + x^15 + x^14 + x^13 + x^12 + x^10 + x^9 + x^8 + x^2 + x^1 + x^0'
poly = 'x^56 + x^55 + x^54 + x^50 + x^44 + x^42 + x^41 + x^40 + x^38 + x^34 + x^31 + x^27 + x^22 + x^21 + x^20 + x^18 + x^16 + x^14 + x^13 + x^12 + x^8 + x^7 + x^6 + x^4 + x^2 + x^1 + x^0'

data = map(lambda x: int(x[2:]), poly.split(' + '))
res = 0
for d in data:
    res |= 1<<d
print(hex(res))
print(long_to_bytes(res))
