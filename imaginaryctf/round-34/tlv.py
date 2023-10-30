from pwn import *
b = bytes.fromhex('01040802130504017B0201020102141202011301020E0C04015F01011302011801020F0404015F01060B040D06130704015F010515000B140404015F020513180F041204015F03030104010102000104017D')
#import tlv8
#for x in tlv8.decode(b):
#    print(xor(x.data, 0x08^0x69))
i = 0
while i < len(b):
    t = b[i]
    l = b[i+1]
    i += 2
    d = b''
    while i < len(b) and len(d) < l:
        d += bytes([b[i]])
        i += 1
    print('type=',t,'len=',l,'data=',d)
