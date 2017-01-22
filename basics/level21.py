import re
import bz2
import zlib

file = open('d:/20/package.pack', 'rb')
data = file.read()
file.close()

result =[]

while True:
    try:
        data = zlib.decompress(data)
        result.append(' ')
    except:
        try:
            data = bz2.decompress(data)
            result.append('a')
        except:
            result.append('\n')
            data = data[::-1]
            try:
                data = zlib.decompress(data)
                result.append(' ')
            except:
                try:
                    data = bz2.decompress(data)
                    result.append('a')
                except:
                    break

print(''.join(result))