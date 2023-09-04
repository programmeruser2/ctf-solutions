from Crypto.Util.number import long_to_bytes
n = int(input('n = '))
e = int(input('e = '))
c = int(input('c = '))
print('decrypt this:')
print((pow(2,e,n) * c) % n)
twom = int(input('2m = '))
print(long_to_bytes((twom * pow(2,-1,n)) % n))
# picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_1772735}

