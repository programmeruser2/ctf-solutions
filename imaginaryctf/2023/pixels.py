from PIL import Image
img = Image.new(mode='RGBA', size=(690, 420))
img.putpixel((412, 309), (52, 146, 235, 123))
img.putpixel((12, 209), (42, 16, 125, 231))
img.putpixel((264, 143), (122, 136, 25, 213))
img.save('img.png', 'PNG')

import os
os.system("exiftool -PNG:Description='jctf{not_the_flag}' -PNG:Title='kool_pic' -PNG:Author='anon' img.png")
