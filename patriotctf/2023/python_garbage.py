import random
random.seed(10)
def finalstage_inv(w):
    res = ''
    h = 0 
    while h < len(w):
        try:
            res += w[h+1] + w[h]
        except:
            res += w[h]
        h += 2
    w = list(res)
    w.reverse()
    return ''.join(w)
def stage2_inv(b):
    t = ''
    for i in range(len(b)):
        t += chr(ord(b[i]) + random.randint(0,5))
    return t 
def stage1_inv(a):
    res = ''
    for i in range(len(a)):
        res += chr(ord(a[i]) ^ i)
    return res 
def entry_inv(f):
    f = list(f)
    f.reverse()
    return ''.join(f)
ct = r'^seqVVh+]>z(jE=%oK![b$\NSu86-8fXd0>dy'
pt = entry_inv(stage1_inv(stage2_inv(finalstage_inv(ct))))
print(pt)

