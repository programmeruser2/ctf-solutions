import sys
sys.set_int_max_str_digits(100000)

r = IntegerModRing(10 ** 10000)
t = Matrix(r, [
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,1],
  [55692,-9549,301,21]
])
f = Matrix(r, [
  [1], 
  [2],
  [3],
  [4]
])
k = 2 * (10**7)
p = t**k 
res = p*f 
print(res[0][0])


