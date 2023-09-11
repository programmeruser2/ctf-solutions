n = 0x575ccba5eb432070f54b12237b91996ff33d9e8fd7c8766da0833a89fd1d95abda573a9e6973c7769f60de749cd044a5d50c62f929680eeb44c0b93b014c1bfdbf668f581a2bfa034c09b2f6b755f8ffe883b5b4e756621b983967e64d728f09f1e8485672b896550928bcab85e72569d140e8e2ddf79dde58a6f6bbcae9c4ae6e8b93e4dc882e0da5ab78a07a92b4257564b34a64b7b19d91f1dac8e695f9b988c49063d72a891762c08683bdee592ff7ce8bd5906a671ea8ea5a54c65211a7182f628e5aa87ad3d388be3fae703ed8c43df264c33dd4c8d6faf3d8571b5c220c05f14093a72b93fe0d93d73b1440fdad30e310daa87e566219b82217d0895d
c = 0x307652ee5a77dab4e70ded15e2c791c268e2c2e389d1f02887ea5baf8cf2b4aab98b4c9c47556a3c4b98c668a90d856c548c574dfa9e252fb92c1886d0fb54ef2492de80879ed5c655ed7e3edebb748599ce2f5d6efaf3843818571d96c92a072f8d7d246c7f440001b5b9e75d6736bb96549e35b45f8e2ba7c133d9238b997c0a6c88a8748e086432017566a372b3defe3c070d0f68694eb3e3c1dd4d12942769d619ec214b6ec1a2d269b81363f5f4866ea8558bb10b22659069001083f45445031a9612df9cf9ee8cc905529e98b4d8c079fd1876d3f03b49c16f2105d3ca5fd9e0b14e777a678d6951aa9c92a35313ce444320e57b17e034ee6278926345

from primefac import pollard_pm1, primefac
from math import ceil, sqrt
from Crypto.Util.number import long_to_bytes

def crt(residues):
    while len(residues) > 1:
        (r1, m1) = residues[-1]
        (r2, m2) = residues[-2]
        residues.pop()
        residues.pop()
        i1 = pow(m1, -1, m2)
        i2 = pow(m2, -1, m1)
        mn = m1*m2 
        rn = (r1 * m2 * i2 + r2 * m1 * i1) % mn
        residues.append((rn, mn))
    return residues[0]

def bsgs(g, a, p, order):
    # p doesn't have to be prime
    # I just made the variable p when I was first writing this
    m = ceil(sqrt(order))
    table = {}
    for j in range(0, m):
        table[pow(g,j,p)] = j 
    cur = a
    gm_inv = pow(g, -m, p)
    for i in range(0, m):
        j = table.get(cur, None)
        if j != None:
            return i*m+j
        else:
            cur *= gm_inv 
            cur %= p
    return None
def pohlig_hellman(g, a, p):
    order = p-1
    factorization = {}
    for pi in primefac(order):
        factorization[pi] = factorization.get(pi, 0) + 1 
    residues = []
    for pi, ei in factorization.items():
        p_e = pow(pi, ei)
        no_p = order // p_e
        gi = pow(g, no_p, p_e)
        hi = pow(a, no_p, p_e)
        # pray that sqrt(order of the group) isn't huge
        p_ord = (p_e // pi) * (pi - 1)
        xi = bsgs(gi, hi, p_e, p_ord)
        residues.append((xi, pi))
    print(residues)
    (x, _) = crt(residues)
    return x

p = pollard_pm1(n)
q = n // p 
print(f'{p = }')
print(f'{q = }')
x1 = pohlig_hellman(3, c, p)
print(f'{x1 = }')
x2 = pohlig_hellman(3, c, q)
print(f'{x2 = }')
(flag_long, _) = crt([ (x1,p-1), (x2,q-1) ])
print(long_to_bytes(flag_long))

