#http://www.pythonchallenge.com/pc/return/romance.html
import urllib
import urllib.request
import http.cookiejar
import bz2


prefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
u = prefix + '12345'

cookies = []
i =0
while False :

    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    print(u)

    r = opener.open(u)
    cookie = r.info().get('Set-Cookie')
    cookies.append(cookie[5:cookie.find(';')])
    response = r.read().decode()

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

cookiestring = ''.join(cookies)
print(cookiestring)

cookiestring = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"

b =urllib.parse.unquote_to_bytes(cookiestring)
print(b.count(b'+'))
b = b.replace(b'+',b' ', 1)

print(len(b))
print(type(b))
print(b)

"""
f1 = open('d:/tmp.1', 'w')
f1.write(b)
f1.close()
"""

print(bz2.decompress(b))

req = urllib.request.Request('http://www.pythonchallenge.com/pc/stuff/violin.php')
req.set_proxy('proxy.sybase.com:8080', 'http')
req.add_header('cookie', 'info=the flowers are on their way')
print(urllib.request.urlopen(req).read())
