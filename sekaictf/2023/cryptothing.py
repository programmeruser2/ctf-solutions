from z3 import *
import string
s = Solver()

non_printable = [i for i in range(255) if chr(i) not in string.printable]

buffer_0_4 = BitVec('buffer_0_4', 32)
s.add(buffer_0_4 > 0)
for i in non_printable:
    s.add(buffer_0_4 & 0xff != i)
    s.add(((buffer_0_4 >> 8  ) & 0xff) != i)
    s.add(((buffer_0_4 >> 16 ) & 0xff) != i)
    s.add(((buffer_0_4 >> 24 ) & 0xff) != i)
    


buffer_4 = BitVec('buffer_4', 32)
s.add(buffer_4 < 255)
s.add(buffer_4 > 0)
for i in non_printable:
    s.add(buffer_4 != i)


buffer_5 = BitVec('buffer_5', 32)
s.add(buffer_5 < 255)
s.add(buffer_5 > 0)
for i in non_printable:
    s.add(buffer_5 != i)

buffer_6 = BitVec('buffer_6', 32)
s.add(buffer_6 < 255)
s.add(buffer_6 > 0)
for i in non_printable:
    s.add(buffer_6 != i)
#
# uVar1 = (uint)(buffer._0_4_ * 0x193482ba) >> 0xf | buffer._0_4_ * 0x5740000;
var1 = BitVec('var1', 32)
s.add(var1 > 0)
s.add(var1 == (buffer_0_4 * 0x193482ba) >> 0xf | buffer_0_4 * 0x5740000)
#
# uVar2 = (uint)buffer[4] ^ (uint)buffer[6] << 0x10 ^ (uint)buffer[5] << 8;
var2 = BitVec('var2', 32)
s.add(var2 > 0)
# s.add(var2 == buffer_4 ^ buffer_6 << 0x10 ^ buffer_5 << 8)
#
# uVar1 = (uVar2 * 0x193482ba >> 0xf | uVar2 * 0x5740000) * 0x59d87c3f ^ (uVar1 * -0x3c1e0800 | uVar1 * 0x59d87c3f >> 0x15) * 7 + 0x47c8ac62
var3 = BitVec('var3', 32)
s.add(var3 > 0)
s.add(var3 == (var2 * 0x193482ba >> 0xf | var2 * 0x5740000) * 0x59d87c3f ^
      (var1 * -0x3c1e0800 | var1 * 0x59d87c3f >> 0x15) * 7 + 0x47c8ac62)

# uVar1 = (uVar1 >> 0x10 ^ uVar1 ^ 7) * 0x764521f9;
var4 = BitVec('var4', 32)
s.add(var4 > 0)
s.add(var4 == (var3 >> 0x10 ^ var3 ^ 7) * 0x764521f9)

# uVar1 = (uVar1 ^ uVar1 >> 0xd) * -0x6c53e18a;
var5 = BitVec('var5', 32)
s.add(var5 > 0)
s.add(var5 == (var4 ^ var4 >> 0xd) * -0x6c53e18a)

s.add((var5 ^ var5 >> 0x10) == 0xf99c821)


print(s.model)
print(s.check())
m = s.model()
print(m)
flag = int(hex(m[buffer_0_4].as_long())[2:] +
           hex(m[buffer_4].as_long())[2:] +
           hex(m[buffer_5].as_long())[2:] +
           hex(m[buffer_6].as_long())[2:],16).to_bytes(7, 'big')
print(flag)

