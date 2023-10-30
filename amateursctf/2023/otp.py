with open('out.txt', 'r') as f:
    ct = bytes.fromhex(f.read())
print(ct)
