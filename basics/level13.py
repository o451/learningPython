#http://www.pythonchallenge.com/pc/return/disproportional.html
#http://www.pythonchallenge.com/pc/return/evil4.jpg
#huge:file

import xmlrpc
import xmlrpc.client
w = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(w.phone('Bert'))