#http://www.pythonchallenge.com/pc/hex/speedboat.html
#import PIL
from PIL import Image,ImageSequence
img = Image.open('d:/zigzag.gif')
w = img.width
h = img.height
print(w,h)
print(img.mode)
data = img.getdata()

palette = img.getpalette()
print(len(palette))
print(palette)
tra = palette[::3]
img.close()

file = open('d:/zigzag.gif', 'rb')
data = file.read()
print(data)

bytes.maketrans()

file.close()