code = open('strange.txt').read()
parts = code.split(',')[1:]
print(len(parts))
for part in parts:
    print(','+part)
