#http://www.pythonchallenge.com/pc/return/mozart.html
import PIL
from PIL import Image
imagePath = 'C:/Users/i074912/Desktop/mozart.gif'

img = Image.open(imagePath, 'r')
print(img.size)
print(img.mode)
print(img.format)
w = img.size[0]
h = img.size[1]
f = Image.new(img.mode, img.size)
for j in range(h) :
    tmp = []
    t1 = []
    findPink = False
    for i in range(w):
        p = img.getpixel((i, j))
        if(p != 195 and not findPink):
            t1.append(p)
        else:
            findPink = True
            tmp.append(p)
    t2 = tmp + t1
    for i in range(w):
        f.putpixel((i, j),t2[i])

f.show()
#img.show()

#f.show()
