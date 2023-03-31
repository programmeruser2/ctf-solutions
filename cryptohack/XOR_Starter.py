data = b'label'
flag = b'crypto{'
for b in data:
    flag += bytes([b ^ 13])
flag += b'}'
print(flag)
