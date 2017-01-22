#http://www.pythonchallenge.com/pc/return/balloons.html
import urllib
import PIL
from PIL import Image
import difflib

file = open('C:/Users/Ming Dai/Desktop/deltas/delta.txt')

left = []
right = []
while True :
    try:
        line = file.readline()
        if len(line)==0 :
            break
        left.append(line[:53])
        right.append(line[56:-1])

    except :
        print("xxxxxxxxxx")
        break
file.close()
print(left)
print(right)
res = list(difflib.ndiff(left, right))
print(res)
e1,e2,e3 = [],[],[]

for i in res :
    if(i[0] == '+') :
        b1 = i[1:].split()
        for k in b1:
            f = bytes.fromhex(k)#bytes(int(k, 16))
            e1.append(f)
    if(i[0] =='-'):
        b2 = i[1:].split()
        for k in b2:
            f = bytes.fromhex(k)
            e2.append(f)
    if(i[0] ==' ') :
        b3 = i[1:].split()
        for k in b3:
            f = bytes.fromhex(k)
            e3.append(f)
g1 =open('d:/1.png', 'wb')
g1.write(b''.join(e1))
g1.close()
#g1.show()

g2 =open('d:/2.png', 'wb')
g2.write(b''.join(e2))
g2.close()

g3 =open('d:/3.png', 'wb')
g3.write(b''.join(e3))
g3.close()


