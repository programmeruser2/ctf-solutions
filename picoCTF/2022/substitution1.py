substitution = {
	'M': 'P',
	'K': 'I',
	'W': 'C',
	'R': 'O',
	'Y': 'T',
	'H': 'F',

	'A': 'R',

	'F': 'Q',
	'B': 'U',

	'L': 'N',
	'U': 'Y',
	'C': 'K',

	'I': 'A',
	'Q': 'B'
}
ciphertext = 'mkwrWYH{HA3FB3LWU_4774WC5_4A3_W001_7II384QW}'
plaintext = ''
for c in ciphertext:
	c = c.upper()
	plaintext += substitution.get(c, c)
print(plaintext)
