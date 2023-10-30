from base64 import b64decode
data = 0x89cb5f6de8a783e9629a2b5e77eb68fa89e5cbeb617be6dab1eeb8f9c85aaec7adfa48a775afacb9c92c
b64 = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
while data > 0:
    b64 = [data%64] + b64
    data //= 64 
print(b64)
b64 = ''.join(map(lambda x: alphabet[x], b64))
print(b64)
print(b64decode(b64))
