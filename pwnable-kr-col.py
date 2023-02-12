from pwn import *
hashcode = 0x21DD09EC
part = hashcode // 5
mod = hashcode % 5
string = bytearray()
for _ in range(4):
	string.extend(p32(part))
string.extend(p32(part+mod))
print(str(string))
# run on remote: ./col $(echo -n -e "<OUTPUT BYTES>")
