# broken rn (need to account for shifts)
from string import ascii_uppercase
ct = open('ciphertext.txt').read()
cols = ['']*13
i = 0 
base = 0 
for c in ct:
    if c in ascii_uppercase:
        cols[i]+=c 
    else:
        cols[i]+='?'
    i=(i+1)%13
#print(cols)
print('\n'.join(cols))
res = ['#']*len(ct)
for i in range(13):
    s = input()
    diff = 0 
    for c in s:
        res[diff+i] = c 
        diff += 13 
print(''.join(res))
