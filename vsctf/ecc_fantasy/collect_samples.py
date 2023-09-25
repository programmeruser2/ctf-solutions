from pwn import *
from tqdm import tqdm
#context.log_level = 'debug'
def parse_point(s):
    return ' '.join(s.decode().strip()[1:-1].split(' : ')[:-1])
r = remote('vsc.tf', 3462)
samples = (624 * 32) // 256 
output = ''
for _ in tqdm(range(samples)):
    r.recvuntil(b'Your choice: ')
    r.sendline(b'1')
    r.recvuntil(b'p = ')
    p = int(r.recvline())
    r.recvuntil(b'P = ')
    P = parse_point(r.recvline())
    r.recvuntil(b'Q = ')
    Q = parse_point(r.recvline())
    output += f'{p} {P} {Q}\n'
r.recvuntil(b'Your choice:')
r.sendline(b'2')
r.recvuntil(b': ')
secret = int(r.recvline(), 16)
r.close()
with open('samples.txt', 'w') as f: 
    f.write(output)
with open('secret.txt', 'w') as f:
    f.write(str(secret))

