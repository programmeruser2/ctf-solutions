ct = b'jU5t_a_sna_3lpm18gb41_u_4_mfr340'
pt = bytearray(32)
for i in range(31, 17-2, -2):
	#print(i)
	pt[i] = ct[i]
for i in range(0, 8):
	pt[i] = ct[i]
for i in range(8, 16):
	pt[i] = ct[23-i]
for i in range(16, 32, 2):
	pt[i] = ct[46-i]
print(pt)
assert b'\x00' not in pt
print('picoCTF{'+pt.decode()+'}')

