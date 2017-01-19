import PIL
from PIL import Image
p = 'C:/Users/i074912/Desktop/oxygen.png'
file = Image.open(p)

f1 = file.crop((0, 43, 608, 52))
#f1.show()
d = f1.getdata()
length = len(d)
s = ''
for i in range(0, length, 7) :
    s = s + chr(d[i][1])
print(s)
file.close()

t = [105, 110, 116, 101, 103, 114, 105, 116, 121]
e = []
for j in t :
    e.append(chr(j))
print(''.join(e))