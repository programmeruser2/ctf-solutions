from re import search 
from requests import Session 
s = Session()
host = 'https://asymmetric-encryption.crypto.w3challs.com'
text = s.get(host + '/').text 
#print(text)
h = int(search(r'h = (\d+)', text).group(1))
f = int(search(r'f = (\d+)', text).group(1))
C = int(search(r'C : (\d+)', text).group(1))
g = pow(f, -1, h)
pt = (C*g)%h 
print(s.post(host + '/index.php?p=solution', data={'mess': str(pt)}).text)



