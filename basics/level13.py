#http://www.pythonchallenge.com/pc/return/disproportional.html
#http://www.pythonchallenge.com/pc/return/evil4.jpg
#huge:file

import xmlrpc
import xmlrpc.client
import http


class ProxiedTransport(xmlrpc.client.Transport):

    def set_proxy(self, host, port=None, headers=None):
        self.proxy = host, port
        self.proxy_headers = headers

    def make_connection(self, host):
        connection = http.client.HTTPConnection(*self.proxy)
        connection.set_tunnel(host, headers=self.proxy_headers)
        self._connection = host, connection
        return connection

transport = ProxiedTransport()
transport.set_proxy('proxy.sybase.com', 8080)

w = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php", transport)
#print(w.phone('Bert'))
print(w.phone('Leopold'))

