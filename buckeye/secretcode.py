from pwn import *
ct = bytes.fromhex(''.join('1:10:d0:10:42:41:34:20:b5:40:03:30:91:c5:e1:e3:d2:a2:72:d1:61:d0:10:e3:a0:43:c1:01:10:b1:b1:b0:b1:40:9'.split(':')))
#partial = xor(b'bctf{', ct[:5])
#print(partial)
#for i in range(0, len(ct)-5):
#    print(xor(ct,partial+b'\x00'*i))
print(xor(ct,b'snub_wrestle'))

