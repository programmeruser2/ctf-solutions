from PIL import Image 
img1 = Image.open('scrambled1.png')
img2 = Image.open('scrambled2.png')
res = Image.new('RGBA', (img1.size[0], img1.size[1]))
px1 = img1.load()
px2 = img2.load()
respx = res.load()
for i in range(res.size[0]):
	for j in range(res.size[1]):
		px = tuple(map(lambda a: a[0]^a[1], zip(px1[i,j], px2[i,j])))
		if px != (255, 255, 255):
			respx[i,j] = (0,0,0)
		else:
			respx[i,j] = (255, 255, 255)
res.save('result.png')

