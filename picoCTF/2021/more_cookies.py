from base64 import b64decode, b64encode
from requests import get 
from tqdm import tqdm
from time import sleep
cookie = 'K253OE91Y0VrV0RjQW5aWnNJZU9yZGFKYVNrNWpLSWgrUzhDVHVxMlZ6MnIvZUJtSURqVWVkY0R4UGhRbytHcTJ2WmQ4Z0M4LzJrcW5mOXRTVUJ3OHliMDBnT3ZIQjliR2JxUDFEbU5BQ1ViV1ZZTHRTM2pnb0dGWUQxZmplNCs='
ct = b64decode(b64decode(cookie))
endpoint = 'http://mercury.picoctf.net:43275/'
done = False
for i in tqdm(range(0, len(ct))):
    for j in tqdm(range(0, 256), leave=False):
        new_ct = bytearray(ct)
        new_ct[i] ^= j
        new_cookie = b64encode(b64encode(new_ct)).decode()
        #print(new_cookie)
        r = get(endpoint, cookies={'auth_name': new_cookie})
        if not 'Only the admin' in r.text:
            print(r.text)
            print(new_cookie)
            done = True 
            break 
    if done:
        break


