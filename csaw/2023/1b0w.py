def get_bits(n):
    bits = []
    for _ in range(29):
        b = n & 1 
        bits = [b] + bits 
        n >>= 1
    return bits
data = '''533258111
274428993
391005533
391777629
390435677
273999169
534074751
99072
528317354
446173689
485174588
490627992
105525542
421383123
132446300
431853817
534345998
496243321
365115424
302404521
289808374
1437979
534308692
272742168
391735804
391385911
391848254
273838450
534645340'''.split('\n')
data = list(map(lambda x: get_bits(int(x)), data))
print(data)

#from pyzbar.pyzbar import decode
from PIL import Image
img = Image.new('RGB', (29, 29))
for y in range(0, 29):
    for x in range(0, 29):
        pixel = (255,255,255) if not data[y][x] else (0,0,0)
        img.putpixel((x,y), pixel)
img.save('qrcode.png')
# for some reason this doesn't detect the qr code
#print(decode(img))

