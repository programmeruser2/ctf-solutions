from base64 import b64decode, b64encode
from requests import get 
from tqdm import tqdm
from time import sleep
cookie = "ckh0cUpySCsxODFxNHVTd05abHd4djZiYmJYRkxHMjhjbGJXWDN1bEFZRFdvYmpWNm9NeWNYT3JNS1BUUnk2ZmJ2eGtMNzBhTFFCRXpESFJFWGZyblh3Q1F0M3NhZTFKSGdhY0ZtT0NTcmhlU3Y3Z2Q3ZVM4eEdWWERqcCtnM2Y="
ct = b64decode(b64decode(cookie))
endpoint = 'http://mercury.picoctf.net:43275/'
for i in tqdm(range(0, len(ct))):
    for j in tqdm(range(0, 256), leave=False):
        new_ct = bytearray(ct)
        new_ct[i] ^= j
        new_cookie = b64encode(b64encode(new_ct)).decode()
        #print(new_cookie)
        r = get(endpoint, headers={'Cookie': 'auth_name='+new_cookie})
        if not 'Only the admin' in r.text:
            print(r.text)
            print(new_cookie)
            break 


