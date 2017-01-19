#http://www.pythonchallenge.com/pc/return/5808.html
import PIL
from PIL import Image

img = Image.open('d:/cave.jpg')
print(type(img))
print(img.size)
print(img.mode)
data = list(img.getdata());
print(type(data))
print(len(data))
d1 = Image.new(img.mode,(img.size[0], img.size[1]))
d2 = Image.new(img.mode,(img.size[0], img.size[1]))

for i in range(img.size[0]) :
    for j in range(img.size[1]) :
        p = img.getpixel((i, j))
        if i%2 ==0 and j%2 ==0 :
            d1.putpixel((i//2, j//2), p)
        elif i%2 ==0 and j%2 ==1 :
            d2.putpixel((i//2, j//2), p)
        if i%2 ==1 and j%2 ==0 :
            d2.putpixel((i//2, j//2), p)
        elif i%2 ==1 and j%2 ==1 :
            d1.putpixel((i//2, j//2), p)

img.show()
#d2.show()