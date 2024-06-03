from pwn import *
with open('challengefile', 'rb') as f:
    data = bytearray(f.read())
for i in range(0, len(data), 4):
    #print(i)
    if i+3>=len(data): continue
    data[i:i+4] = p32(u32(data[i:i+4], endianness='big'), endianness='little') 
with open('endianv2.jfif', 'wb') as f:
    f.write(data)
