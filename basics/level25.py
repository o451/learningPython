#http://www.pythonchallenge.com/pc/hex/lake.html
#butter:fly

import PIL,wave
import urllib
import urllib.request
from PIL import Image
import base64

img = Image.open('d:/lake1.jpg')
#print(img.size)
#print(img.mode)
#print(img.format)

data = img.getdata()
#print(len(data))
#print(type(data))
w = img.width
h = img.height
#print(w,h)

urltemplate = 'http://www.pythonchallenge.com/pc/hex/lake{0}.wav'
localfiletemplate = 'd:/level25/{0}.wav'
localimgtemplate = 'd:/level25/{0}.bmp'

"""
for i in range(1,26) :
    pwdMsg = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pwdMsg.add_password(None, urltemplate.format(i), 'butter', 'fly')
    auth = urllib.request.HTTPBasicAuthHandler(pwdMsg)
    __opener = urllib.request.build_opener()
    __opener.add_handler(auth)
    urllib.request.install_opener(__opener)
    urllib.request.urlretrieve(urltemplate.format(i), localfiletemplate.format((i)))
"""

pics = []
for i in range(1, 26) :
    wav = wave.open(localfiletemplate.format(i))
    print(wav.getnframes())
    print(wav.getnchannels())
    print(wav.getcompname())
    print(wav.getcomptype())
    print(wav.getframerate())
    print(wav.getmarkers())
    d = wav.readframes(wav.getnframes())
    print(d)
    image = Image.frombytes('RGB', (60,60), (d))
    #image.save(localimgtemplate.format(1))
    pics.append(image)
    #image.close()

large = Image.new('RGB', (300, 300))
for j in range(5):
    for i in range(5):
        large.paste(pics[i*5+j], (j*60, i*60))

large.save('d:/level25/large.bmp')
large.close()