from linalg import Vector 
v = [
    Vector([4,1,3,-1]),
    Vector([2,1,-3,4]),
    Vector([1,0,-2,7]),
    Vector([6,2,9,-5])
]
u = [v[0]]
for i in range(1, len(v)):
    s = Vector([0,0,0,0])
    for j in range(i):
        tmp = v[i].dot(u[j]) / u[j].dot(u[j])
        s += tmp*u[j]
    u.append(v[i] - s)

print(u)
print(u[3][1])


