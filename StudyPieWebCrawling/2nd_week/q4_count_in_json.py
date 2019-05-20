import urllib.request
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_353540.json', context=ctx).read()
json_file = data.decode('utf-8')

json_data = json.loads(json_file)

sum_of_count = 0
for item in json_data['comments']:
    sum_of_count += item['count']

print('Sum of count is', sum_of_count)
