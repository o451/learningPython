#http://www.pythonchallenge.com/pc/hex/decent.html
import email,smtplib,poplib
import email.mime
#from email.mime import MIMEText

"""smtp = smtplib.SMTP()
#msg = MIMEText('sorry')
msg = "From: o451@hotmail.com\r\nTo: leopold.moz@pythonchallenge.com\r\nSubject: sorry\r\n\r\n"
smtp.connect('smtp-mail.outlook.com:587')
smtp.ehlo()
smtp.starttls()
smtp.login('o451@hotmail.com','xxxxxx')
smtp.sendmail('o451@hotmail.com', 'leopold.moz@pythonchallenge.com', msg)
smtp.close()
"""
import hashlib
import sys
f = open('d:/24/mybroken.zip', 'rb')
data = f.read()
for j in range(256):
    print(j)
    for i in range(len(data)):
        newdata = data[:i] + int.to_bytes(j, 1, sys.byteorder) + data[i+1:]
        #print(hashlib.md5(newdata).hexdigest())
        if hashlib.md5(newdata).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
            g = open('d:/24/new.zip', 'wb')
            g.write(newdata)
            g.close()
            print('found')
            break


