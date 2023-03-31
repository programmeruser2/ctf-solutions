from pwn import *
ciphertext = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
start = b'crypto{'
end = b'}'
# <known> ^ <ciphertext>
keystart = b''
keyend = b''
for i in range(len(start)):
    keystart += bytes([start[i] ^ ciphertext[i]])
for i in range(len(end)):
    keyend += bytes([end[i] ^ ciphertext[-i-1]])
print('keystart =', keystart)
print('keyend =', keyend)
# output: 
# keystart = "myXORke"
# keyend = "y"
# so the key is probably "myXORkey"
print(xor(ciphertext, b'myXORkey'))
