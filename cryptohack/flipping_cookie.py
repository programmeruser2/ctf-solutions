from pwn import xor 
cookie = bytes.fromhex('0d3fdbcaed78f79d35344c6a56df0a53572868a7ac5bb1a72b016c58471d6826fc339faaf15772722241f735e097d820')
orig_iv = cookie[:16]
ct = cookie[16:]

orig = b'False'
target = b'True;'
diff = xor(orig, target, orig_iv[6:11])
iv = orig_iv[:6]+diff+orig_iv[11:]
print('iv:', iv.hex())
print('ct:', ct.hex())
# crypto{4u7h3n71c4710n_15_3553n714l}
