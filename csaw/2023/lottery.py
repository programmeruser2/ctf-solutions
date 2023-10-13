from pwn import *
context.log_level = 'debug'
r = remote('crypto.csaw.io', 5000)
def sendn(n):
    r.sendlineafter(b'>> ', str(n).encode())

tickets = 35
sendn(tickets)

pairings = []
for i in range(1, 69+1):
    for j in range(i+1, 69+1):
        pairings.append((i,j))

i = 0
for _ in range(tickets):
    s = set()
    while len(s) < 6:
        olds = s.copy()
        a, b = pairings[i]
        i += 1
        s.add(a)
        s.add(b)
    assert(len(s) == 6)
    print(s)

    #print(s)
    for x in s:
        sendn(x)
    


r.interactive()
