from pwn import *
from longest_increasing_subsequence import longest_increasing_subsequence_indices
r = remote('chal.amt.rs', 1410)
#r = process(['python3', './lis-server.py'])
t = int(r.recvline())
print(t, 'test cases')
#input('press to continue')
#context.log_level='debug'
for _ in range(t):
    print('we are on iteration', _)
    data = r.recvline()
    #print('data', data)
    if _ == 100: print(data)
    elements = list(map(int, data.split()))
    solver = process('./lis')
    solver.sendline(str(len(elements)).encode())
    solver.send(data)  
    res=solver.recvline()
    print('res',res)
    assert len(res.split())==len(longest_increasing_subsequence_indices(elements))
    r.send(res)
    solver.close()
    #input('press to continue')
print('we are done')
#print(r.recvall())
r.interactive()

