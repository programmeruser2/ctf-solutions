from linalg import Vector, gaussian_reduction
v = Vector((846835985, 9834798552))
u = Vector((87502093, 123094980))
res = gaussian_reduction(v,u)
print(res[0].dot(res[1]))
