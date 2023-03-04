from pwn import *
r = remote('saturn.picoctf.net', 53865)
for i in range(5):
	r.sendline(b'1')
	r.sendline(b'rockpaperscissors')

#r.interactive()
# Interactive doesn't work here either for some reason
print(r.recvuntil('}'))
