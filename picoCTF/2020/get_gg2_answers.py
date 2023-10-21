from pwn import * 
import tqdm
context.log_level = 'error'
start = -4096
for i in tqdm.tqdm(range(start, 4096)):
    try:
        r = remote('jupiter.challenges.picoctf.org', 18263)
        r.recvuntil(b'!')
        r.sendline(str(i).encode())
        s = r.recvuntil(b'!')
        #print(s)
        r.close()
        if b'Congrats' in s:
            print(i)
            break
    except Exception as e:
        print(e)
        print('stopped at', i)
        exit(1)


