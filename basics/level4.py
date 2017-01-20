import urllib
import urllib.request
import http.cookiejar

prefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
u = prefix + '12345'
#for i in range(1,400) :
i =0
while True :

    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    print(u)



    #opener = urllib.request.HTTPCookieProcessor()
    #urllib.request.install_opener(opener)
    r = opener.open(u)
    response = r.read().decode()

    if(cj) :
        print(cj)

    print(response)
    r.close()

    try :
        last = response[response.rfind(' ') + 1: ]
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
