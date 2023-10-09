import math
class Matrix:
    def __init__(self,vals):
        self.vals = vals
    def __getitem__(self, x):
        return self.vals[x]
    def __add__(self, v):
        return Matrix([[self.vals[i][j]+v[i][j] for j in range(len(v[i]))] for i in range(len(v))])
    def __neg__(self):
        return Matrix([[-x for x in r] for r in self.vals])
    def __sub__(self,v):
        return self + (-v)
    def __mul__(self,x):
        return Matrix([[i*x for i in r] for r in self.vals])
    __rmul__ = __mul__
    def __truediv__(self,x):
        return self*(1/x)
    def __len__(self):
        return len(self.vals)
    def __str__(self):
        return str(self.vals)
    def __repr__(self):
        return repr(self.vals)
    def det(self):
        assert len(self) == len(self[0])
        if len(self) == 0: return 1
        if len(self) == 1: return self[0][0]
        if len(self) == 2:
            return self[0][0]*self[1][1]-self[0][1]*self[1][0]
        s = 0 
        m = 1 
        for i in range(len(self)):
            s += m*self[0][i]*Matrix([r[:i] + r[i+1:] for r in self.vals[1:]]).det()
            m *= -1
        return s 
class Vector(Matrix):
    def __init__(self, vals):
        if type(vals) == tuple:
            vals = list(vals)
        self.vals = [vals]
    def __getitem__(self, x):
        return self.vals[0][x]
    def __len__(self):
        return len(self.vals[0])
    # use the correct class for results
    def __add__(self, v):
        return Vector([v[i]+self[i] for i in range(len(v))])
    def __neg__(self):
        return Vector([[-x for x in r] for r in self.vals][0])
    def __mul__(self,x):
        return Vector([[i*x for i in r] for r in self.vals][0])
    __rmul__ = __mul__
    def dot(self,v):
        return sum([self[i]*v[i] for i in range(len(v))])
    def __str__(self):
        return str(tuple(self.vals[0]))
    def __repr__(self):
        return repr(tuple(self.vals[0]))
    def norm(self):
        return math.sqrt(self.dot(self))
    def normalize(self):
        f = self.norm()
        return self / f 
     
def gaussian_reduction(v1, v2):
    while True:
        if v2.norm() < v1.norm():
            v1, v2 = v2, v1
        m = round(v1.dot(v2) / v1.dot(v1))
        if m == 0:
            return v1, v2
        v2 = v2-m*v1

