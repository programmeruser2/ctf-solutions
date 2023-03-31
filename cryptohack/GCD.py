def gcd(a, b):
    x = min(a, b)
    y = max(a, b)
    while x != 0:
        y, x = x, y % x
    return y
print(gcd(66528, 52920))
