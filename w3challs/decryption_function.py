def encrypt(x):
	y = ''
	for c in x:
		y += chr(ord('A') + ((21*(ord(c)-ord('A'))+11) % 26))
	return y

def decrypt(x):
	y = ''
	for c in x:
		y += chr(ord('A') + ((5*(ord(c)-ord('A'))+23) % 26))
	return y

s = ''

s += encrypt('GOOGLE').lower()
s += '_5y+23[26]_'
s += decrypt('GELKT').lower()

print(s)
