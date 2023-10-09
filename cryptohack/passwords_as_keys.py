from Crypto.Cipher import AES 
from hashlib import md5
with open('words') as f:
    words = [w.strip() for w in f.readlines()]
ct = bytes.fromhex('c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66')
for w in words:
    key = md5(w.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    flag = cipher.decrypt(ct)
    if b'crypto{' in flag:
        print(flag)
        break
