from primefac import primefac 
p = 28151
factors = set(primefac(p-1))
def is_primroot(g):
    for f in factors:
        if pow(g, (p-1)//f, p) == 1:
            return False 
    return True 
for g in range(2, p):
    if is_primroot(g):
        print(g)
        break
