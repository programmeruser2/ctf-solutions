from pwn import * 

for i in range(1, 4096):
    r = remote('jupiter.challenges.picoctf.org', 18263)
    r.recvuntil(b'!')
    r.sendline(str(i).encode())
    s = r.recvuntil(b'!')
    #print(s)
    r.close()
    if b'Congrats' in s:
        print(s)
        break

