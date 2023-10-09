p = 2525114415681006599
f = GF(p)
x0 = f(2029673067800379268)
y0 = f(1814239535542268363)
x1 = f(602316613633809952)
y1 = f(1566131331572181793)
iv = bytes.fromhex('6959dbf6bf22344d452c3831a3b68897')
enc = bytes.fromhex('a490e177c3838c8f24d36be5ee10e0c9e244ac2e54cd306eddfb0d585d5f27535835fab1cd83d26a669e6c08096b58cc4cc4cb082f4534ce80fab16e21f119adc45a5f59d179ca3683b77a942e4cf4081e01d921a51ec3a3a48c13f850c04b80c997367739bbde0a5415ff921d77a6ef')
# recover the equation in weierstrass form
a = ((y0**2 - y1**2) - (x0**3 - x1**3)) * (x0-x1)^-1
b = (y0**2 - (x0**3 + a*x0))
C = EllipticCurve(f, [a, b])
seed = C.gens()[0]
p0 = C(x0, y0)
p1 = C(x1, y1)
# the lcg equation simplifies to a(x_0 - seed) = x_1 - x_0 
# since p-1 is smooth, we can do a discrete log quickly 
# let aP = Q 
P = p0 - seed 
Q = p1 - p0 
a = P.discrete_log(Q)
b = p0 - a*seed 
# now we just have to decrypt the ciphertext 
from Crypto.Cipher import AES 
from Crypto.Util.number import long_to_bytes 
from Crypto.Util.Padding import pad, unpad
prng_next = a * p1 + b 
v = prng_next[0]
k = pad(long_to_bytes(int(v)**2), 16)
cipher = AES.new(k, AES.MODE_CBC, iv=iv)
flag = unpad(cipher.decrypt(enc), 16)
print(flag)


