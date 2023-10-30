from Crypto.Util.number import long_to_bytes
fac = [2, 3, 19, 31, 83, 3331, 165219437, 550618493, 66969810339969829, 1168302403781268101731523384107546514884411261]
ct = 6954494065942554678316751997792528753841173212407363342283423753536991947310058248515278

def search(n, fp):
    if n == len(fac):
        sp = ct // fp
        flag = long_to_bytes(fp) + long_to_bytes(sp)
        if flag.startswith(b'DUCTF{'):
            print(flag.decode())
            exit(0)
        return
    search(n+1, fp)
    search(n+1, fp*fac[n])
search(0, 1)


