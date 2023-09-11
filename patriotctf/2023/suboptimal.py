target = b'xk|nF{quxzwkgzgwx|quitH'
flag = b''
for c in target:
    c -= 8
    if c < 0x41:
        c += 0x3d 
    flag += bytes([c])
print(flag)
