from z3 import *
ct = bytearray(b'\x18j|a\x118i7O\x09~\x0e8L\x04n\x5c\x14\x1bz><\x1d\x08q\x044J\x5cg\x0aA\x17|c`\x17]+TZ')
for i in range(0, len(ct), 2):
    if i+1 >= len(ct): continue
    ct[i], ct[i+1] = ct[i+1], ct[i]
inp = ct
flag = b''
for i in range(len(ct)):
    val = inp[i] ^ 0x14
    if i > 0:
        val ^= inp[i-1]
    if i > 2:
        val ^= inp[i-3]
    val ^= i % 10
    if i % 2 == 0:
        val ^= 9
    else:
        val ^= 8 
    if i % 3 == 0:
        val ^= 7 
    elif i % 3 == 1:
        val ^= 6 
    else:
        val ^= 5
    flag += bytes([val])
print(flag)
    
