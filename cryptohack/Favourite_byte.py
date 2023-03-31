from pwn import *
ciphertext = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
for key in range(0,255+1):
    plaintext = xor(ciphertext, key)
    if plaintext.startswith(b'crypto{'):
        print(f'possible: key={hex(key)}, plaintext="{plaintext}"')
