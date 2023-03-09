ciphertext = 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2'
plaintext = ''
for i in range(0, int(len(ciphertext)/3)):
	plaintext += ciphertext[i*3 + 2]
	plaintext += ciphertext[i*3 + 0]
	plaintext += ciphertext[i*3 + 1]
print(plaintext)
