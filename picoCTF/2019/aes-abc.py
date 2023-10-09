# from the provided file
import math
BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))
def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index(b'\n') + 1], s[s.index(b'\n')+1:]
def parse_header_ppm(f):
    data = f.read()

    header = b""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data
header, data = parse_header_ppm(open('body.enc.ppm', 'rb'))
blocks = [data[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE] for i in range(len(data)//BLOCK_SIZE)]
orig = blocks.copy()
for i in range(len(blocks)-1, 0, -1):
    blocks[i] = ((int(blocks[i].hex(),16)-int(blocks[i-1].hex(),16)) % UMAX).to_bytes(BLOCK_SIZE, 'big')
c_img = b''.join(blocks)
#print(data[:50], c_img[:50])
with open('body.ecb.ppm', 'wb') as f:
    f.write(header)
    f.write(c_img)

