#http://www.pythonchallenge.com/pc/hex/ambiguity.html
import PIL,sys,array,zipfile
from PIL import Image
img = Image.open('d:/maze1.png')
w = img.width
h = img.height
print(w,h)

wall = (255,)*4

for x in range(w):
    p = img.getpixel((x,0))
    q = img.getpixel((x, h-1))
    if p != wall :
        START = (x,0)
    if q != wall :
        END = (x,h-1)

print(START, END)

openset = []
direction =((-1,0),(1,0),(0,1),(0,-1))

def checkPoint (current, prev) :
    foundDoor = False
    for d in direction:
        point = (current[0] + d[0], current[1] + d[1])
        if point == prev:
            continue
        try:
            p = img.getpixel(point)
            if p == wall:
                continue
            else:
                openset.append((current, point))
                foundDoor = True
        except:
            continue
    return foundDoor

checkPoint(START, START)
while True :
    item = openset[-1]
    nextPoint = item[1]
    if(nextPoint == END) :
        break;

    doorFound = checkPoint(nextPoint, item[0])
    if not doorFound:
        img.putpixel(nextPoint, wall)
        openset.pop()

print(openset[:10])
points = [END]
pathImage = Image.new(img.mode, img.size)
pathImage.putpixel(END, wall)
current = END
while item[0] != START :
    item = openset.pop()
    if item[1] == current :
        pathImage.putpixel(item[0], wall)
        points.insert(0,item[0])
        current = item[0]
    else:
        print('found non-path ' + str(item[0]))
else :
    print(item)
#pathImage.show()

img.close()
img = Image.open('d:/maze1.png')

p1 = []
z =open('d:/24.zip', 'wb')
for point in points:
    p = img.getpixel(point)
    p1.append(int.to_bytes(int(p[0]), 1, sys.byteorder))
    print(int.to_bytes(int(p[0]), 1, sys.byteorder))
    #p1.append(chr(int(p[0])))
    #p1.append(p[0])
img.close()
#assert(d1 == "\x00" * len(d1))
#print(len(p1))
#data = array.array("B", p1)
#z.write(data[1::2])
z.write(b''.join(p1[1::2]))
z.close()
print('end is found')

#with zipfile.ZipFile('d:/24.zip') as u :
#    print(u)

