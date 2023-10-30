from ctypes import CDLL
import tqdm
libc = CDLL('libc.so.6')
partial = b'ictf{'
with open('out.bin', 'rb') as f:
    enc = f.read()
for seed in tqdm.tqdm(range(0, (1<<32)-1)):
    libc.srand(seed)
    works = True
    for i, c in enumerate(partial):
        newc = c
        for j in range(i+1):
            newc = newc ^ (libc.rand() & 0xff)
        if newc != enc[i]:
            works = False
            #print('fail on',i)
            break
    if not works:
        continue
    print('found match:', seed)
    libc.srand(seed)
    flag = b''
    for i, c in enumerate(enc):
        newc = c
        for j in range(i+1):
            newc = newc ^ (libc.rand() & 0xff)
        flag += bytes([newc])
    print(flag)
    ok = input('ok? ')
    if ok == 'y':
        break

