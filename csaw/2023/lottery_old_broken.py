from pwn import *
context.log_level = 'debug'
r = remote('crypto.csaw.io', 5000)
tickets = 30
r.sendlineafter(b'>> ', str(tickets).encode())
seq = list(range(1, 69+1))
for _ in range(0, (tickets*6) // 69):
    for i in range(0, 69):
        r.sendlineafter(b'>> ', str(seq[i]).encode())
for i in range(0, (tickets*6) % 69):
    r.sendlineafter(b'>> ', str(seq[i]).encode())

r.interactive()
