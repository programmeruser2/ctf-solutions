import hashlib
hashed = '''523c
4b29
5b51
c419
409a
b5fd
136d
802b
5b51
523c
136d
7713
8542
39f3
136d
23cd
39f3
8542
cd00
136d
5b51
136d
8542
523c
23cd
8542
23cd
24b9
b58a
e08d
5b51
523c
b58a
e08d
23cd
8542
3744
24b9
24b9
cd00
8542
e08d
f233
24b9
fee3
3744
39f3
8542
7955
d481
8e8f
65a1
42d6
01d4'''.split('\n')
# generate lookup table
lookup = {}
for c in range(0, 255+1):
    lookup[hashlib.sha256(bytes(c)).hexdigest()[:4]] = chr(c)
flag = ''
for line in hashed:
    flag += lookup[line]
print(flag)
