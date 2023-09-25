key = bytearray([0]*39)
key[0:4] = b's3cR'
key[4:8] = b'3ts3'
key[0xa:0xa+4] = b'vsct'

tmp = b"fvsctiamfrnow0kkeyw0wkeyw"
key[0xa+4:0xa+4+len(tmp)] = tmp 
key[0x14:0x14+len(tmp)-5] = tmp[5:]
key[0x14+len(tmp)-5:0x14+len(tmp)-5+len(tmp)-10] = tmp[10:]
key[0x1e:0x1e+len(tmp)-0xf] = tmp[0xf:]
key[0x1e+len(tmp)-0xf:0x1e+len(tmp)-0xf+len(tmp)-0x14] = tmp[0x14:]

print(f'{key = }')

target = [None]*53
part1 = b'\x7e\x7b\x6b\x7c\x6e\x73\x7f\x3b\x3c\x63\x57\x3c\x66\x7c\x39\x57\x6c\x3b\x6a\x7d\x6f\x6f\x3b\x7a\x7b\x57'
part2 = b'\x3c\x7a\x3b\x57\x66\x38\x57\x65\x3c\x7c\x6b\x60\x57\x6e\x38\x7a\x57\x7c\x60\x3b\x57\x3b\x39\x3b\x3b\x3f\x75'
for i in range(0, 0x1a):
    target[i] = part1[i]
for i in range(0, 0x1b):
    target[i+0x1a] = part2[i]
print(f'{target = }')
flag = b''
for i in range(0, len(target)):
    flag += bytes([target[i]^0x12^key[0]^key[0xb]^key[0xb*2]^key[0xb*3]])
print(flag)



