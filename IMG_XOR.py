from PIL import Image

img1 = Image.open("file1.png")
img2 = Image.open("file2.png")

w, h = img1.size

pixel1 = img1.load()
pixel2 = img2.load()

for x in range(w):
    for y in range(h):
        r1,b1,g1 = pixel1[x,y]
        r2,b2,g2 = pixel2[x,y]
        r,b,g = r1^r2, b1^b2, g1^g2
        pixel1[x,y] = (r,b,g)

img1.save("out.png")