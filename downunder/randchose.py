import random
ct = open('output.txt').read()
flag_len = len(ct)//5
options = list(range(0, flag_len))
for i in range(0, 1337):
    random.seed(i)
    choices = random.choices(options, k=flag_len*5)
    flag = ['~'] * flag_len
    for j in range(len(choices)):
        flag[choices[j]] = ct[j]
    flags = ''.join(flag)
    if 'DUCTF{' in flags:
        print(flags)
        break
