from pwn import *
key = bytes.fromhex('3836313833366631336533643632376466613337356264623833383932313465')
ct = bytes.fromhex('4a53475d414503545d025a0a5357450d05005d555410010e4155574b45504601')
password = xor(ct,key)
r = remote('mercury.picoctf.net', 4052)
r.sendline(password)
r.sendline(b'goldfish') # MD5("goldfish") -> key 
r.interactive()
