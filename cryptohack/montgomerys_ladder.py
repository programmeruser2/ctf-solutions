from sage.all import *
pr = 2**255-19
B=1 
A=486662
def add(p, q):
    assert p!=q
    alpha=((q[1]-p[1])*pow(q[0]-p[0],-1,pr))%pr
    x=(B*alpha*alpha-A-p[0]-q[0])%pr
    y=(alpha*(p[0]-x)-p[1])%pr
    return (x,y)
def double(p):
    alpha=((3*(p[0]**2)+2*A*p[0]+1)*pow(2*B*p[1],-1,pr))%pr
    x=(B*(alpha**2)-A-2*p[0])%pr
    y=(alpha*(p[0]-x)-p[1])%pr
    return (x,y)
def mont(k, P):
    r0, r1 = P, double(P)
    for i in range(k.bit_length() - 2, 0-1, -1):
        if (k&((1<<i+1)-1))>>i == 0:
            r0, r1 = double(r0), add(r0, r1)
        else:
            r0, r1 = add(r0, r1), double(r1)
    return r0
v=(9**3+A*(9**2)+9)%pr
G=(9,int(Integers(pr)(v).sqrt(v)))
#print(G, double(G))
#print(G,double(G),add(G,double(G)))
print(mont(0x1337c0decafe,G))
