ct = 'apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna'
#ct = 'jeihigidifjgihig'
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
def b16_decode(enc):
    plain = ''
    for i in range(0, len(enc), 2):
        plain += chr((ALPHABET.index(enc[i]) << 4) + ALPHABET.index(enc[i+1]))
    return plain
def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]
#print(b16_decode('gbgbgb'))
#print(unshift('h', 'c'))
for k in ALPHABET:
    r = ''
    for c in ct:
        #print(c)
        r += unshift(c, k)
    r = b16_decode(r)
    if all(c in string.printable for c in r):
        print(r)
