import math
import hashlib
import sys
from tqdm import tqdm
import functools

import numpy as np

ITERS = int(2e7)
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfb5885e6c7ed9a3c62b")
sys.set_int_max_str_digits(0)
#sys.setrecursionlimit(ITERS+5)
# This will overflow the stack, it will need to be significantly optimized in order to get the answer :)
@functools.cache
def m_func(i):
    '''if i == 0: return 1
    if i == 1: return 2
    if i == 2: return 3
    if i == 3: return 4

    return 55692*m_func(i-4) - 9549*m_func(i-3) + 301*m_func(i-2) + 21*m_func(i-1)'''
    # float128 overflows so this doesn't work
    # see sequences.sage
    '''
    m = np.array([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [55692, -9549, 301, 21]
    ], dtype=np.float128)
    p = np.linalg.matrix_power(m, i)
    return int(np.matmul(p, [1, 2, 3, 4])[0])
    '''
    return int(open('sequences.res.txt').read())

#print(m_func(2))
#print(m_func(4), m_func(5), m_func(6), m_func(7), m_func(8), m_func(9), m_func(10), m_func(11), m_func(12))
# Decrypt the flag
def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

if __name__ == "__main__":
    sol = m_func(ITERS)
    #print(sol)
    decrypt_flag(sol)
