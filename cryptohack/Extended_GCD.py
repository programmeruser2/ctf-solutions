def extended_gcd(a,b):
    x1, y1, x2, y2, gcd1, gcd2 = 0, 1, 1, 0, b, a
    while gcd1 > 0:
        q = gcd2 // gcd1
        gcd2, gcd1 = (gcd1, gcd2 - q*gcd1)
        x2, x1 = x1, x2 - q*x1
        y2, y1 = y1, y2 - q*y1
    return (x2, y2)
print(extended_gcd(26513, 32321))

