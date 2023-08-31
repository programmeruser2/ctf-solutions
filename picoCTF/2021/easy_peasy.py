from pwn import *
KEY_LEN = 50_000
r = remote('mercury.picoctf.net', 11188)
r.recvuntil(b'flag!\n')
ct = bytes.fromhex(r.recvline().strip().decode())
FLAG_LEN = len(ct)
r.sendline(b'a'*(KEY_LEN-FLAG_LEN))
r.recvuntil(b'Here ya go!\n')
r.sendline(b'a'*FLAG_LEN)
r.recvuntil(b'Here ya go!\n')
enc_res = bytes.fromhex(r.recvline().strip().decode())
key = xor(enc_res, b'a'*FLAG_LEN)
print('flag:', 'picoCTF{' + xor(ct, key).decode() + '}')





