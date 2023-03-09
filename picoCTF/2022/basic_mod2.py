def mod_inverse(n, m):
	for i in range(1, m):
		if (n*i) % m == 1:
			return i
ciphertext = "104 85 69 354 344 50 149 65 187 420 77 127 385 318 133 72 206 236 206 83 342 206 370"
plaintext = ''
for i in ciphertext.split(' '):
	n = mod_inverse(int(i), 41)
	if n <= 26:
		plaintext += chr((n - 1) + 65)
	elif n <= 36:
		plaintext += chr((n - 27) + 48)
	else:
		plaintext += '_'
print(f'picoCTF{{{plaintext}}}')
