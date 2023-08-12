fruits = [
    '110006170013060408131904',
    '1715141100190814130818181',
    '40214141100130305201308',
    '111421041100061700130604'
]
flag = 'LITCTF{'

for fruit in fruits:
    n = fruit 
    if len(n) % 2 != 0:
        # check which side needs padding with zeroes, and add if needed
        v = int(n[0] + n[1])
        if v <= 25:
            n += '0'
        else:
            n = '0' + n
    for i in range(0, len(n), 2):
        flag += chr(ord('a') + int(n[i] + n[i+1]))

question = '6954957548549661084455388'
for d in question:
    flag += chr(ord('a') + int(d))

flag += '}'
print(flag)

