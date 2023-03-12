# p+q = x
# pq = n
# -> q = x-p
# -> p(x-p) = n
# -> -p^2 + xp - n = 0
# solve with quadratic formula in O(1) time
# the two roots will be p and q
from math import sqrt
import gmpy2
x = 0x1797321ba57f9d58ab3bbaaad0d857748c4fbde6d16447c5b785e16c9a2e69ad30f596b35810499e9b301700ed8d722b5352a867e48283eedfd879ab397bbb36182f38675bb2aa83973c0ea3c2773da576813a004661d3e5db4e03e9a90b4d76693f0daae2730394e7f1977e2587ca71e700c85fcba1c888c128e02fcd23f7dba
n = 0x8656b782764c0b446ab555e4f1b0a0866f2038f4aaaa26c33f83897805fb1290b762c830ecff842e504e202c3625695768612add7dfee92cb2faaa6e0906d9da0b5c4d5815fd4e2d73b648154f0728c644e2d1fcec8d4bea953e49ad89d2f21d0d240f191a229daeb2c10534542c74f50d1fbb09db7bd4085a36a7870c726219576029c53b9471ffee5f9ab51a713c7a7e44c9a9eee60abcbfdb4461aff4e94c77b0f243f3455b853a32ca0d819c66aef6907c479c127b465b8fbfc77030dc0e59e4c676def55f9787df04c9594bfee6286d4d8c395db30884133693c3ea56e7b4e35709d4e1e65c7ee75fc794025cd8929217f1ae3c4f4a191a7b858cf3f125

discriminant = x*x - 4*(-1)*(-n)
discriminant_sqrt = gmpy2.isqrt(discriminant)
p = (-x+discriminant_sqrt)//(-2)
q = (-x-discriminant_sqrt)//(-2)
print(f'p = {p}')
print(f'q = {q}')
# you can decode it now with another tool
