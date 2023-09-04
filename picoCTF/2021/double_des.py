from Crypto.Cipher import DES
import string
def decrypt(m, key):
    c = DES.new(key, DES.MODE_ECB)
    return c.decrypt(m)
def encrypt(m, key):
    c = DES.new(key, DES.MODE_ECB)
    return c.encrypt(m)

flag_enc = bytes.fromhex(input('Encrypted flag: '))
pt = b'abcdefgh' + b' '*8
ct = bytes.fromhex(input(f'Encryption result of {pt[:8].hex()}: '))

lookup = {}
def search(n, key, **kwargs):
    # True = forwards, False = backwards
    direction = kwargs['direction'] 
    if n == 6:
        key += b' ' * 2
        if direction:
            enc = encrypt(pt, key)
            lookup[enc] = key 
        else:
            dec = decrypt(ct, key)
            other_key = lookup.get(dec, None)
            if other_key != None:
                print('Match found')
                flag = decrypt(decrypt(flag_enc, key), other_key)
                print('Flag:')
                print(flag)
                exit(0)
        return 
    for d in string.digits:
        search(n+1, key+str(d).encode(), direction=direction)

search(0, b'', direction=True)
print('finished forward search')
#print(lookup)
search(0, b'', direction=False)

"""
Match found
Flag:
b'9af5126b7bc7f825b3cae0e32bd1acb4        '
"""

print('No solutions found')
exit(1)

