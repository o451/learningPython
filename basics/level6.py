import zipfile
from zipfile import ZipFile
from urllib import *

filename = 'C:/Users/i074912/Desktop/channel.zip'
f = zipfile.ZipFile(filename, 'r')
q = '90052.txt'
r1 = []
print(f.comment)
while True:
    l = f.read(q).decode()
    print(l)
    r1.append(f.getinfo(q).comment.decode())
    n = l[l.rfind(' ') +1:]
    try :
        j = int(n)
        q =  n + '.txt'
    except:
        break

print(''.join(r1))
