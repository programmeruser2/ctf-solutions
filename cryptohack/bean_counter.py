from pwn import xor
import requests 
ct = bytes.fromhex(requests.get('https://aes.cryptohack.org/bean_counter/encrypt/').json()['encrypted'])
target = bytes.fromhex('89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52')
key = xor(target, ct[:16])
img = xor(ct, key)
with open('bean_flag.png', 'wb') as f:
    f.write(img)
