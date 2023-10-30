from pwn import *
r = remote('actually-baby-rev.ctf.maplebacon.org', 1337)
# stage 1 
r.sendline(b'5'*19+b'9'*8)
# stage 2 
r.sendline(b'4'*3+b'2'*1)
# stage 3 
r.sendline(b'80673')
# get the flag 
r.interactive()
