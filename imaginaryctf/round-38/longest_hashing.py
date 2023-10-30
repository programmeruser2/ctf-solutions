import random 
from randcrack import RandCrack 
rc = RandCrack()
for _ in range((624 * 32) // 512):
    x = (random.getrandbits(1024)) % (2**512)
    for i in range(512 // 32):
        rc.submit((x >> (i*32)) & 0xFFFFFFFF)

print(rc.predict_getrandbits(1024))
print(random.getrandbits(1024))
