import random
import math
import hashlib
p = int(input('p='))
msg = b'a'
k = random.randint(2,p-2)
while math.gcd(k,p-1) != 1:
    k = random.randint(2,p-2)
print('k=',k)
r = pow(g,k,p)
s = int(hashlib.sha256(msg).hexdigest()[:12],16) - 
if s == 0:
    print('fail s=0')
else:
    print(r,s)
