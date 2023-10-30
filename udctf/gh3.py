from pwn import *
from string import printable
printable = printable.encode()
ct = bytes.fromhex('98edbf5c8dd29e9bbc57d0e2990e4e692efb81c2318c69c626d7ea42f2efc70fece4ae5c89c7999fef1e8bac99021d7266bc9cde3cd97b9a2adaeb08dea1ca0582eaac13ced7dfdbad1194b1c60f5d372eeec29832ca20d12a85b545f9f69b1aaeb6ec4cd4')
clue = b'https://gist.github.com/AndyNovo'
#for i in range(0,2):
for i in range(0, len(ct)-len(clue)):
    skey = xor(ct[i:i+len(clue)], clue)
    key = skey[len(clue)-i:] + skey[:len(clue)-i]
    #print(skey, key)
    pt = xor(key, ct)
    if all(c in printable for c in pt): print(pt)
