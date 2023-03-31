from pwn import *
import json
r = remote('socket.cryptohack.org', 11112)
r.sendline(json.dumps({'buy': 'flag'}))
r.interactive()
