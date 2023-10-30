from z3 import *

def to32bit(x):
    return x & 0xFFFFFFFF
class SymbolicPythonMT19937(object):
    def __init__(self, seed):
        self.seed = seed
        self.state = [None]*624

        self.f = 1812433253
        self.n = 624
        self.m = 397
        self.r = 31
        self.u = 11
        self.s = 7
        self.a = 0x9908B0DF
        self.b = 0x9D2C5680
        self.t = 15
        self.c = 0xEFC60000
        self.l = 18
        self.w = 32 
        self.d = 0xFFFFFFFF

        self.index = self.n
        self.lower_mask = (1 << self.r)-1
        self.upper_mask = 1 << self.r 

        # converted from the cpython sources
        # init the generator 
    
        i = 1
        self.state[0] = BitVecVal(19650218, 32)
        for mti in range(1, self.n):
            self.state[mti] = to32bit(self.f * (self.state[mti-1] ^ LShR(self.state[mti-1], 30)) + mti)
        #print([simplify(x) for x in self.state])
        for k in range(self.n, 0, -1):
            #print(self.state[i], self.state[i-1], seed)
            #print( (self.state[i] ^ ((self.state[i-1] ^ LShR(self.state[i-1], 30)) * 1664525)) )
            self.state[i] = (self.state[i] ^ ((self.state[i-1] ^ LShR(self.state[i-1], 30)) * 1664525)) + seed
            i += 1 
            if i >= self.n: 
                self.state[0] = self.state[self.n-1]
                i = 1 
        for k in range(self.n-1, 0, -1):
            self.state[i] = simplify(to32bit(
                (self.state[i] ^ ((self.state[i-1] ^ LShR(self.state[i-1], 30)) * 1566083941)) - i
            ))
            i += 1 
            if i >= self.n:
                self.state[0] = self.state[self.n-1]
                i = 1 
        self.state[0] = BitVecVal(0x80000000, 32)
        
    def __iter__(self):
        return self
    def twist(self):
        for i in range(0, self.n):
            x = (self.state[i] & self.upper_mask) + (self.state[(i+1)%self.n] & self.lower_mask)
            xA = LShR(x, 1)
            self.state[i] = simplify(self.state[(i+self.m)%self.n] ^ If(x&1 != 0, xA^self.a, xA))
    def __next__(self):
        if self.index >= self.n:
            self.twist()
            self.index = 0
        y = self.state[self.index]
        y ^= LShR(y, self.u)&self.d 
        y ^= (y<<self.s)&self.b 
        y ^= (y<<self.t)&self.c 
        y ^= LShR(y, self.l)
        self.index += 1
        return simplify(to32bit(y))

s = Solver()
seed = BitVec('seed', 32)

import random
random.seed(0x0)
set_param('parallel.enable', True)
set_option(verbose = 10)
r = SymbolicPythonMT19937(seed)
for _ in range(1):
    nxt = next(r)
    print(nxt)
    s.add(nxt == random.getrandbits(32))
print('solving')
if s.check() == sat:
    m = s.model()
    print(m[seed])

