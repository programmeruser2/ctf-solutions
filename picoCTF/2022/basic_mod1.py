ciphertext = "91 322 57 124 40 406 272 147 239 285 353 272 77 110 296 262 299 323 255 337 150 102"
plaintext = ''
for i in ciphertext.split(' '):
	n = int(i) % 37
	if n <= 25:
		plaintext += chr((n - 0) + 65)
	elif n <= 35:
		plaintext += chr((n - 26) + 48)
	else:
		plaintext += '_'
print(f'picoCTF{{{plaintext}}}')
