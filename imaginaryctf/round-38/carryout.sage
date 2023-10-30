import string
field = PolynomialRing(GF(2), 'x')
x = field.gen()
p = x^124 + x^120 + x^117 + x^114 + x^112 + x^110 + x^109 + x^108 + x^107 + x^106 + x^105 + x^102 + x^100 + x^94 + x^93 + x^89 + x^85 + x^82 + x^81 + x^80 + x^78 + x^77 + x^76 + x^74 + x^68 + x^67 + x^61 + x^56 + x^54 + x^52 + x^48 + x^46 + x^45 + x^43 + x^40 + x^38 + x^36 + x^29 + x^28 + x^18 + x^17 + x^14 + x^12 + x^10 + x^9 + x^6 + x^5 + x
f = p.factor()
results = {}
for mask in range(0, 1<<len(f)):
  prod = x^0
  for i in range(len(f)):
    if mask & (1<<i):
      prod *= (f[i][0] ** f[i][1])
  res = 0
  for e in prod.exponents():
    res |= 1<<e 
  if res > 0xFFFFFFFFFFFFFFFF: continue
  b = int(res).to_bytes(8, 'little')
  results[mask] = b
  if b.startswith(b'{') and all([chr(c) in string.printable for c in b]):
    other = field(p/prod)
    othern = 0
    for e in other.exponents():
      othern |= 1<<e 
    otherb = int(othern).to_bytes(8, 'little')
    print(b'ictf'+b+otherb+b'}')
