import json
import requests, pprint

url = 'https://miffle.braydenlab.com/miffle/file_get_bin.php'
headers = {'content-type': 'application/binary'}

try:
    rawH_file = open('rawHexBPfile.bin', 'rb')
except:
    print('IO error')

files = {'rawHexBPfile': rawH_file}
print(type(rawH_file))

response = requests.post(url, files=files)

pprint.pprint(response.text)
