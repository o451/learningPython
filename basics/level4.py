import urllib
import urllib.request

prefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
u = prefix + '12345'
#for i in range(1,400) :
i =0
while True :

    r = urllib.request.urlopen(u)
    response = str(r.read())
    print(response)
    r.close()

    try :
        last = response[response.rfind(' ') + 1: -1]
        num = last
        if int(num) >0 :
            u = prefix + num
            print(i, u)
            i = i + 1
        succ = num
    except:
        if response.find('Divide') != -1:
            u = prefix + str(int(succ) /2)
        else:
            break
