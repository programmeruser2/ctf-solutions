from pwn import xor
from tqdm import tqdm
import json
import sys
import hashlib

sys.setrecursionlimit(10000)
lock = json.loads(open('jslockdata.txt', 'r').read())

def search(arr, target):
    for i in range(0, len(arr)):
        if type(arr[i]) == int:
            if arr[i] == target:
                if i == 0:
                    return [0]
                else:
                    return [1]*i+[0]
            continue
        elif type(arr[i]) != list:
            return None
        r = search(arr[i], target)
        if r != None:
            if i == 0:
                return [0]+r
            else:
                return [1]*i+[0]+r
    return None

pin = ''
for i in tqdm(range(1, 1337+1)):
    seq = search(lock, i)
    if seq == None:
        raise Exception("Couldn't find sequence for i=" + str(i))
        exit(1)
    pin += ''.join(map(str, seq))

m = hashlib.sha512()
m.update(pin.encode())
hash = m.digest()
ct = [62, 223, 233, 153, 37, 113, 79, 195, 9, 58, 83, 39, 245, 213, 253, 138, 225, 232, 123, 90, 8, 98, 105, 1, 31, 198, 67, 83, 41, 139, 118, 138, 252, 165, 214, 158, 116, 173, 174, 161, 6, 233, 37, 35, 86, 7, 108, 223, 97, 251, 2, 245, 129, 118, 227, 120, 26, 70, 40, 26, 183, 90, 172, 155]
print(xor(ct, hash).decode())
# DUCTF{s3arch1ng_thr0ugh_an_arr4y_1s_n0t_th4t_h4rd_ab894d8dfea17}

