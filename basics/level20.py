#http://www.pythonchallenge.com/pc/hex/idiot2.html
import PIL
import urllib
import base64
import re
from urllib import request

z = open('d:/20.zip', 'wb')
#req.add_header('Accept', '*/*')
begin = 30203
while begin <= 2123456789 :
    req = request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
    req.add_header('Authorization', 'Basic ' + base64.b64encode('butter:fly'.encode()).decode())
    req.add_header('Range', 'bytes=' + str(begin) + '-2123456789')
    #req.add_header('Range', 'bytes=' + '2123456743-2123456789')
    print("requesting " + str(begin))
    try:
        response = urllib.request.urlopen(req)

        ran = response.getheader('Content-Range')
        range = re.findall(' (\\d+)-(\\d+)\/', ran)
        begin = int(range[0][1]) +1
        print(response.read().decode())
    except Exception as e:
        print('cannot open')
        print(str(e))
        print(type(e))
        break

begin = 2123456789
while True:
    req = request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
    req.add_header('Authorization', 'Basic ' + base64.b64encode('butter:fly'.encode()).decode())
    req.add_header('Range', 'bytes=' + str(begin) +'-')
    try:
        response = urllib.request.urlopen(req)

        msg = response.read().decode()
        print(msg)
        ran = response.getheader('Content-Range')
        range = re.findall(' (\\d+)-(\\d+)\/', ran)
        begin = int(range[0][0]) -1
        print(range)
    except Exception as e:
        print('cannot open')
        print(str(e))
        print(type(e))
        break

databe = re.findall('\\d+', msg)
print(databe)

req = request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
req.add_header('Authorization', 'Basic ' + base64.b64encode('butter:fly'.encode()).decode())
req.add_header('Range', 'bytes=' + databe[0] + '-' )
try:
    response = urllib.request.urlopen(req)

    print(response.info())
    z.write(response.read())
except Exception as e:
    print('cannot open')
    print(str(e))
    print(type(e))

z.close()
