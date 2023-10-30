import random 
from string import printable 
import binascii
printable = printable.encode()
ct = binascii.unhexlify('a0469bbb0b3a4f06306739032244b0c5119ba66a0d3b5a2322acdd7070bf85690cdf8573212c1b927e0ba624')
for i in range(-100, 100):
    seed = int(1697043249.53 + i)
    random.seed(seed)
    pt = ''
    for c in ct:
        pt += chr(random.randint(0,255)^ord(c))
    if all(c in printable for c in pt): print(pt)
    
