import pickle
import pprint
f = open('d:/banner.p', 'rb')
result=pickle.load(f)
pprint.pprint(result)
for line in result:
    for i in line :
        print(i[0] * i[1], end = '')
    print()
