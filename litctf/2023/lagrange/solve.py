fruits = '110006170013060408131904171514110019081413081818140214141100130305201308111421041100061700130604'
flag = 'LITCTF{'

for i in range(0, len(fruits), 2):
    flag += chr(ord('a') + int(fruits[i] + fruits[i+1]))

question = '6954957548549661084455388'
for d in question:
    flag += chr(ord('a') + int(d))

flag += '}'
print(flag)

