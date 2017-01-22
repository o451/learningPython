#http://www.pythonchallenge.com/pc/hex/copper.html
#http://www.pythonchallenge.com/pc/hex/white.gif

import urllib
import urllib.request
import PIL
from PIL import Image,ImageSequence

#file = urllib.request.urlopen('http://www.pythonchallenge.com/pc/hex/level22.jpg')

#data = file.read()
img =Image.open('d:/white.gif')
points =[]
print(img.info)
print(img.getbbox())
index = 1
for frame in ImageSequence.Iterator(img):
    #frame.save("d:/frame%d.png" % index)
    for i in range(frame.size[0]):
        for j in range(frame.size[1]):
            p = img.getpixel((i, j))
            if (p != 0):
                points.append((i, j, p))
    index += 1
print(points)
#img.show()

(x,y) = (0,0)
n = Image.new(img.mode,img.size)
for i in points :
    if(i[0]==100 and i[1] ==100) :
        x = x+20
        y = y+20
    x = x + i[0]-100
    y = y + i[1]-100

    if x<200 and x >0 and y<200 and y>0:
        n.putpixel((x,y), 127)
    else:
        print(x,y)
n.show()

img.close()

