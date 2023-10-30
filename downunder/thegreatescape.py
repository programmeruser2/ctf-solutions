from pwn import *
context(arch='amd64', os='linux')
r = remote('2023.ductf.dev', 30010)

