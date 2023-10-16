import string 
import os 
import gdb 
from shlex import quote

#flag = 'picoCTF{'
flag = 'picoCTF{4ny0n3_g0t_r1scv_h4rdw4r3?_LG'
charset = string.printable 
length = 52 
print('starting:', flag)
os.system('killall -9 qemu-riscv64')
while len(flag) < length:
    found = False 
    for c in charset:
        print('testing:', flag+c)
        os.system(f"echo {quote(flag+c)} | qemu-riscv64 -g 1234 ./riscy &") 
        gdb.execute('target remote :1234')
        gdb.execute('b *0x000101d0')
        gdb.execute('c')
        for _ in range(len(flag)): gdb.execute('c')
        a3 = int(gdb.execute('info registers a3', to_string=True).split()[1], 16)
        a4 = int(gdb.execute('info registers a4', to_string=True).split()[1], 16)
        if a3 == a4:
            flag += c 
            found = True 
            break
        gdb.execute('detach')
        os.system('killall -9 qemu-riscv64')
    print('current state:', flag)
    assert found 
    if flag[-1] == '}': break 
print('final flag:', flag)
