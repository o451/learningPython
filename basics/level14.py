#http://www.pythonchallenge.com/pc/return/italy.html

import PIL
from PIL import Image
file = Image.open('d:/wire.png')
print(file.size)
print(file.mode)

img = Image.new(file.mode, (100,100))
a = 100
b = 99
c = 99
d = 98
index = 0
round =0
while a >0 and b>0 and c>0 and d>0:
    try:

        for i in range(a) :
            p = file.getpixel((index, 0))
            index = index +1
            img.putpixel((round+i, round), p)

        for i in range(b) :
            p = file.getpixel((index, 0))
            index = index +1
            img.putpixel((99-round, round+i+1), p)

        for i in range(c) :
            p = file.getpixel((index, 0))
            index = index +1
            img.putpixel((99-i-round-1, 99-round), p)

        for i in range(d) :
            p = file.getpixel((index, 0))
            index = index +1
            img.putpixel((round, 98-i-round), p)

    except:
        print(a , b,c,d)
    a = a-2
    b = b-2
    c = c-2
    d = d-2

    round = round +1

img.show()