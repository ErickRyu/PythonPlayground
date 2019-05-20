import urllib.request
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_42.xml', context=ctx).read()
xml_file = data.decode('utf-8')

stuff = ET.fromstring(xml_file)
lst = stuff.findall('comments/comment')

sum_of_count = 0
for item in lst:
    sum_of_count += int(item.find('count').text)

print('Sum of count is', sum_of_count)
