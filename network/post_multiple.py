import json
import requests, pprint

url = 'https://miffle.braydenlab.com/miffle/file_get_multiple.php'
#url = 'https://miffle.braydenlab.com/miffle/post_php.php'

#headers = {'Content-type': 'multipart/form-data', 'charset': 'UTF-8'}
#headers = {'content-type': 'application/binary'}
#headers = {'Content-type': 'application/json'}

f_json = open('train_condition.json', 'rb')
json_file = json.load(f_json)
#print(type(json_file))

f_bin = open('rawHexBPfile.bin', 'rb')

#files = {'rawHexBPfile': f_bin}

sample = {'a': {'b':'c'}}

files = {
    'json': (None, json.dumps(sample), 'application/json'),
    'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
}


#print(type(sample_json))

#response = requests.post(url, data=sample, files=files, headers=headers)
#response = requests.post(url, data=json_file, files=files)
response = requests.post(url, files=files)

print(response.url)
pprint.pprint(response.text)

