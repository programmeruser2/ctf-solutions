from tqdm import tqdm
load("smart_attack.sage")
seq = []
def process(p, Px, Py, Qx, Qy):
  f = GF(p)
  Px = f(Px)
  Py = f(Py)
  Qx = f(Qx)
  Qy = f(Qy)
  a = ((Py**2 - Qy**2) - (Px**3 - Qx**3)) * (Px - Qx)^-1
  b = Py**2 - (Px**3 + a*Px)
  C = EllipticCurve([a,b])
  bits = attack(C(Px, Py), C(Qx, Qy))
  seq.append(bits)
with open('samples.txt', 'r') as f:
  for _ in tqdm(range(78)):
    p, Px, Py, Qx, Qy = map(int, f.readline().strip().split(' '))
    process(p, Px, Py, Qx, Qy)
output = ''
for x in seq:
  output += str(x) + '\n'
with open('bits.txt', 'w') as f:
  f.write(output)
