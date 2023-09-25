from randcrack import RandCrack 
rc = RandCrack()
with open('bits.txt', 'r') as f:
    for _ in range(78):
        x = int(f.readline().strip())
        for i in range(8):
            rc.submit((x >> (i*32)) & 0xFFFFFFFF)
with open('secret.txt', 'r') as f:
    secret = int(f.read())
a = rc.predict_getrandbits(1337)
b = rc.predict_getrandbits(1337)
flag = (secret - b) // a 
print(bytes.fromhex(hex(flag)[2:]))


