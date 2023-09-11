from pwn import *
from string import printable
def test(s):
    with remote('chal.pctf.competitivecyber.club', 4757) as r:
        r.sendlineafter(b': ', s.encode())
        return len(r.recvall().decode().split('\n'))
flag_len = 19
flag = 'pctf{' + 'a' * (19 - 6) + '}'
for i in range(5, flag_len-1):
    maxlen = -1 
    maxlenf = None 
    for c in printable:
        f = flag[:i] + c + flag[i+1:]
        res = test(f)
        if maxlen == -1:
            maxlen = res 
            maxlenf = f 
            continue
        if res > maxlen:
            flag = f
            break
        elif res < maxlen:
            flag = maxlenf 
            break 
print(flag)
