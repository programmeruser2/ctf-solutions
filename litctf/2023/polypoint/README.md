# crypto/polypoint
If we look at the Python code for encryption, it appears to be using the flag + 10 other random values as the coefficients of the polynomial, and then applying that polynomial to 10 values of `x`:
```python3
from secrets import SystemRandom

gen = SystemRandom()

with open("flag.txt", "rb") as f:
    flag = f.read().strip()

assert len(flag) == 76
c = int.from_bytes(flag)

poly = [c]
for _ in range(10):
    poly.append(gen.randrange(pow(10, 11), pow(10, 12)))

for _ in range(10):
    x = gen.randrange(pow(10, 11), pow(10, 12))
    v = 1
    y = 0
    for i in range(11):
        y += poly[i] * v
        v *= x
    print(f"({x},{y})")
```
The output provides us with those 10 points. This seems pretty hard to solve with standard math. So then I tried Z3, which has a reputation as the universal™ CTF math problem solver. 

First, I created 11 different unknown integers as the coefficients. Then I went through every point and added the input and output values of the polynomial as constraints.

However, it was still giving some negative values as solutions, so I had to further constrain the other 10 variables to make sure it only gave me the correct solution.

This was my solution code:

```python3
from z3 import *
s = Solver()
a1 = Int('a1')
a2 = Int('a2')
a3 = Int('a3')
a4 = Int('a4')
a5 = Int('a5')
a6 = Int('a6')
a7 = Int('a7')
a8 = Int('a8')
a9 = Int('a9')
a10 = Int('a10')
a11 = Int('a11')
points = [(222738709477,316551778779405646458024537762733801628425406461784850075599026498565053741337014147035678112471767302308313353838044031384848988200756445707893827080502933079092477245748936205615933),
(664206699157,316551778779405646458024537762733801628425406461784865888104427550077373548635944879652146674701538655158942462878858974744248309318363468921449484127695581959767202569054993652750413),
(466816971715,316551778779405646458024537762733801628425406461784850540303274228943505333219096607064771157569751164935212810740341383248296484763121216876204976922546302648442276863425162951302531),
(607781685226,316551778779405646458024537762733801628425406461784856583382479099611040995482582095486729568867989002474408931170294156825431149788517895709696274929020833693332497499840363986925099),
(461897022854,316551778779405646458024537762733801628425406461784850493556595331266454714391588455928605071712770811139310679403293828814206705942751367641724970531838791010168761153135360884888535),
(202327489838,316551778779405646458024537762733801628425406461784850075423398238878408230054253297735101192329059219854114270219684709044279114983523359477376014765414249172332168704365910277580351),
(725444534262,316551778779405646458024537762733801628425406461784888271334595529696194192935525696332159935854379702373400181836567569198038350522944722135426814323563038237838302091934606155414343),
(141109996562,316551778779405646458024537762733801628425406461784850075317586071223857237881593915942449100069207516884338864872222789437630103529153819546593153502414706533022296987673577977490643),
(804730347399,316551778779405646458024537762733801628425406461784957840821679977943920236001416214794146567946679239226799972519639121487616962138348188601823466436334038618719972219587477332148495),
(816183152786,316551778779405646458024537762733801628425406461784974198308680985846108087143358779128530920963540979977208391612900806473785228320819563422998987542015274186487481705512333905741139)]
for p in points:
    x = p[0]
    y = p[1]
    s.add(a1*(x**10) + a2*(x**9) + a3*(x**8) + a4*(x**7) + a5*(x**6) + a6*(x**5) + a7*(x**4) + a8*(x**3) + a9*(x**2) + a10*x + a11 == y,
          10**11 <= a1,
          a1 < 10**12,
          10**11 <= a2,
          a2 < 10**12,
          10**11 <= a3,
          a3 < 10**12,
          10**11 <= a4,
          a4 < 10**12,
          10**11 <= a5,
          a5 < 10**12,
          10**11 <= a6,
          a6 < 10**12,
          10**11 <= a7,
          a7 < 10**12,
          10**11 <= a8,
          a8 < 10**12,
          10**11 <= a9,
          a9 < 10**12,
          10**11 <= a10,
          a10 < 10**12)
print(s.check())
if s.check() == sat:
    m = s.model()
    print(m)

print('done solving')
```
Then I just had to run it and get the value of `a11` (the plaintext):
```
sat
[a7 = 935980668626,
 a3 = 955890462020,
 a4 = 454440673026,
 a5 = 452005879133,
 a10 = 313279007477,
 a1 = 946184833449,
 a8 = 271655499806,
 a2 = 732320833166,
 a9 = 757866189843,
 a6 = 459744599602,
 a11 = 316551778779405646458024537762733801628425406461784850075314624284410512205504185854127162483240834258174499942538442249509701418557132428064898960083863248218687532418743039826290301]
done solving
```
Lastly you just have to run the output through CyberChef (or whatever your preferred tool of choice is), [converting to hex and then to raw bytes from the hex values](https://gchq.github.io/CyberChef/#recipe=To_Base(16)From_Hex('Auto')&input=MzE2NTUxNzc4Nzc5NDA1NjQ2NDU4MDI0NTM3NzYyNzMzODAxNjI4NDI1NDA2NDYxNzg0ODUwMDc1MzE0NjI0Mjg0NDEwNTEyMjA1NTA0MTg1ODU0MTI3MTYyNDgzMjQwODM0MjU4MTc0NDk5OTQyNTM4NDQyMjQ5NTA5NzAxNDE4NTU3MTMyNDI4MDY0ODk4OTYwMDgzODYzMjQ4MjE4Njg3NTMyNDE4NzQzMDM5ODI2MjkwMzAx), and I got the flag: `LITCTF{h4h4_1ts_n0t_th4t_345y__almOst_ThEre_hAVe_somE_gibbeRish__d6570c3b3f}`.