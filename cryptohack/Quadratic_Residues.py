p = 29
ints = [14, 6, 11]
for n in ints:
    for a in range(0, int((p-1)/2)+1):
        if (a*a - n) % p == 0:
            print(f'{a}^2 = {n} (mod {p})')
