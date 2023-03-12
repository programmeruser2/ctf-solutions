from PIL import Image
import sys
if len(sys.argv) < 2:
	print('usage: St3g0.py <image path>')
	exit(0)

img = Image.open(sys.argv[1])
bits = []
data = img.getdata()

for i in range(0, len(data)):
	for j in range(0, 3):
		bits.append(data[i][j]&0x1)

message = ''
for i in range(0, int(len(data)/8), 8):
	message += chr(int(''.join([str(x) for x in bits[i:i+8]]), 2))
print(message)
