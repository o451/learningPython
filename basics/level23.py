#http://www.pythonchallenge.com/pc/hex/bonus.html
import string
s = 'va gur snpr bs jung'
t = 'abcdefghijklmnopqrstuvwxyz'

for i in range(26):
    trans = s.maketrans(t, t[i:]+t[:i])
    print(t[i:]+t[:i])
    s.translate( trans)
    print(s.translate(trans))