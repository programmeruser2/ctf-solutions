from z3 import *
import requests
def solve(l):
    assert l % 6 == 0 
    s = Solver()
    inp = []
    for i in range(l):
        byte = BitVec("%s" % i, 8)
        s.add(byte <= 122, byte >= 97)
        inp.append(byte)

    conds = []
    for i in range(0, l, 6):
        add = inp[i]&inp[i+2]
        orv = inp[i+1]|inp[i+4]
        xor = inp[i+3]^inp[i+5]
        conds.append(If(And(add == 0x60, orv == 0x61, xor == 0x6), add+orv-xor, 0))
    s.add(Sum(conds) == 0xbb)
    sols = []
    while s.check() == sat:
        sol = b''
        m = s.model()
        for i in range(l):
            sol += bytes([m[inp[i]].as_long()])
        neq = []
        for i in range(l):
            neq.append(inp[i] != sol[i])
        s.add(Or(*neq))
        sols.append(sol.decode())
    return sols 
def check_password(pwd):
    endpoint = 'http://chal.pctf.competitivecyber.club:9096/check.php'
    r = requests.post(endpoint, data={'password': pwd})
    if 'incorrect' in r.text:
        return False
    return r.text 

l = 6 
total = 0
while True:
    sols = solve(l)
    print(f'{len(sols)} solution(s) of length {l}, currently tested {total} solutions(s)')
    for pwd in sols:
        res = check_password(pwd)
        if res != False:
            print(f'password = {pwd}')
            print(res)
            exit(0)
    l += 6
    total += len(sols)
