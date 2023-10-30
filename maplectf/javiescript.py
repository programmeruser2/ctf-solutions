from hashlib import sha256
from itertools import permutations
from tqdm import tqdm
import string
part1 = 'maple{b'
part2 = 'annnnas_are_a_mId_FruiT}'
target = bytes.fromhex('bfe06d1e92942a0eca51881a879a0a9aef3fe75acaece04877eb0a26ceb8710d')
charset = string.ascii_letters + string.digits + '_'
l = 1 
pbar = tqdm()
while True:
    perms = [''.join(p) for p in permutations(charset, l)]
    found = False
    for p in tqdm(perms, leave=False):
        #print(p)
        if sha256((part1+p+part2).encode()).digest() == target:
            print()
            print(part1+p+part2)
            found = True
            break
    pbar.update(1)
    l += 1
    if found:
        break
pbar.close()

