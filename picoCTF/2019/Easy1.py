def alpha_to_number(c):
	return ord(c)-ord('A')
ciphertext = 'UFJKXQZQUNB'
key = 'SOLVECRYPTO'
plaintext = ''
for i in range(len(ciphertext)):
	plaintext += chr((alpha_to_number(ciphertext[i]) - alpha_to_number(key[i])) % 26 + ord('A'))
print(f'picoCTF{{{plaintext}}}')

