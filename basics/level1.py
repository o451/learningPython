import string
a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
#a = 'map'
print(a)
b = list(a)
print(b)
index = 0
d = ''

for i in b :
    if i == 'z':
        b[index] = 'b'
        index = index +1
        continue
    if i == 'y':
        b[index] = 'a'
        index = index +1
        continue
    if i not in string.ascii_letters :
        index = index +1
        continue

    b[index] = chr(ord(i) +2)
    index = index +1

print(b)
c = tuple(b)
print(c)

for i in c :
    d = d + i
print(d)

