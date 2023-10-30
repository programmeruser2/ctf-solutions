from math import sin, pi 
from tqdm import tqdm
ct = b"\xca\xae`fg\x94\x88d\xfe'ut|\x1a\x11_\xd4\xc2UmK\xb4\xcf_\x13\x1dy_\x87\x1a\x00_\xd5\xb3MnK\xbe\xd8i\x0c\x14}ns)\x07e\xc0\x8ei"
key = 0 
def get_shift(i):
    return int(256*sin(key*(i+1)/256*pi))
#bar = tqdm()
#s = set()
while (ct[0] - get_shift(0)) % 256 != ord('i') or key == 32:
    #s.add(get_shift(0))
    #print(len(s))
    key += 1  
    #bar.update(1)
#bar.close()
print(f'{key = }')
flag = b''
for i in range(len(ct)):
    flag += bytes([(ct[i] - get_shift(i)) % 256])
print(flag)
