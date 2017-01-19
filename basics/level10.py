#a = [1, 11, 21, 1211, 111221 ]
import re

def desc(s) :
    f = re.findall("""(1+|2+|3+|4+)""", s)
    r = ''
    for i in f :
        r =r + str(len(i)) + i[0]
    print(r)
    return r

s = '1'
for i in range(30) :
    print(i)
    s = desc(s)
print(len(s))