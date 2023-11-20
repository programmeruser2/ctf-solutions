xor_key = b'\x3f\x65\x93\xfe\x5a\x97\xa1\x50\x6b\x0e\x91\x16\xf9\x2c\xdc\x87\xfd\x45\x7a\x8c\x7e\x56\x1f\x82\xc8\x86\xdf\xf0\x24\x48\x5f\x34\x25\x6d\x43\x83\x01\xdc\xf4\xc1\x94\xce\xc8\x8c\x3e'
key = b'\x56\xf3\xb4\x56\x45\x8f\xb9\xcc\x51\xf9\x95\x68\x2f\x76\x9d\x98\x47\x91\x7a\x91\x56\x5f\x98\x85\xbd\xbf\xea\x04\xae\x23\x2b\x31\xdb\x93\xed\xbf\x2b\x9c\xe7\x0f\x30\xbc\xb5\x75\x6d' 
sbox = b'\xe1\x2c\x8f\x12\x4f\x79\xce\x29\xd5\x5e\xf3\x43\x1c\xd9\x80\xdc\xa7\x8d\x35\xb8\x9a\xed\x0e\x22\x51\xcd\xb7\x25\x18\x68\xaa\xa6\x70\xf4\x52\xe3\x15\xca\xde\x36\x09\xdd\xb5\x72\x05\x62\xe7\xe5\xee\xf0\x76\xd3\xd6\x21\x57\x1b\xa0\x32\x17\x7c\xbe\x10\x8c\xc6\x9f\xe8\xfa\x7a\x26\x03\x01\x88\x7b\x59\x9e\x54\x75\x60\x3a\x63\x30\xa9\x33\xaf\x41\x6e\x92\x87\x95\x6d\x64\x58\x0f\x98\xdb\xe2\xa1\x00\x48\x7e\x0a\xd8\x3b\xc9\xf9\x89\x7d\x08\xf1\xec\x5f\xda\x13\xc4\xb4\x0b\x47\x93\xab\x5c\x44\xf5\x61\xbd\x4c\xc0\x78\x96\x0d\x6a\x3f\x0c\x34\xba\xc1\x86\x45\x31\x71\xcb\x4b\xe0\x23\xb9\x94\xe9\x5d\x3e\x82\xbb\xf8\x3c\xf7\xd2\x1d\x84\xa8\x81\x74\xcc\x38\x9b\xff\x20\x97\x7f\xfd\x6b\xdf\x40\xb2\xd4\x55\x50\x73\x1a\x24\xa5\xc3\x4d\x2e\x4e\xeb\x04\x42\x5a\xfe\x02\xe6\xf6\xef\xb3\x14\xea\xc8\xb6\x67\xa4\xb1\x5b\xcf\x77\xbc\x90\x66\x19\x39\xa2\x37\xfc\x65\x99\x49\x85\xad\x1f\xac\x3d\x9d\x56\xbf\x2d\x2a\x9c\xb0\xf2\x53\x07\x8a\x8b\xa3\x2b\x2f\xc7\x1e\x91\x69\x46\x11\x4a\x28\xc2\x6f\x06\xd1\xe4\x8e\x16\xc5\xd7\x27\x6c\xfb\xae\x83\xd0'
key = bytearray(key)
def twist():
    for i in range(0, 0x2d):
        key[i] = sbox[key[i]]

flag = b''
for i in range(0, 0x2d):
    flag += bytes([key[i] ^ xor_key[i]])
    twist()
print(flag)