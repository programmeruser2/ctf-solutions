from random import randint
from longest_increasing_subsequence import longest_increasing_subsequence_indices
def gen(a, b):
    r=[]
    for _ in range(randint(1,int(1e5))):
        r.append(randint(1,int(1e5)))
    return r
def solve(arr):
    return longest_increasing_subsequence_indices(arr)

