from sympy import fft, ifft 
# source: https://cp-algorithms.com/algebra/fft.html#implementation
MOD=7514777789
def polymul(a, b):
    n = 1
    while n<(len(a)+len(b)): n<<=1 
    a+=[0]*(n-len(a))
    b+=[0]*(n-len(b))
    fa = fft(a)
    fb = fft(b)
    for i in range(n):
        fa[i] *= fb[i]
    inv = ifft(fa)
    result=[]
    for i in range(0, n):
        result.append(round(fa[i].real())%MOD)
    return result 
points=[]

#source: flag_printer.py 
for line in open('encoded.txt', 'r').read().strip().split('\n'):
    x, y = line.split(' ')
    points.append((int(x),int(y)))
print(len(points))
# optimized lagrange interpolation
#


