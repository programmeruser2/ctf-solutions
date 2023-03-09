alphabet = 'QWITJSYHXCNDFERMUKGOPVALBZ'
ciphertext = '5PW5717P710E_3V0DP710E_03055505'
plaintext = ''
for c in ciphertext:
	if c.isalpha():
		plaintext += chr(alphabet.index(c) + 65)
	else:
		plaintext += c
print(f'picoCTF{{{plaintext}}}')
