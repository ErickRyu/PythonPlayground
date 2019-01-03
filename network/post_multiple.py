import json
import requests, pprint

# url = 'https://miffle.braydenlab.com/miffle/file_get_multiple.php'
# url = 'https://miffle.braydenlab.com/miffle/post_php.php'
url = 'https://miffle.braydenlab.com/miffle/get_files_and_calc.php'

f_json = open('train_condition.json', 'rb')
f_bin = open('rawHexBPfile.bin', 'rb')

json_file = json.load(f_json)
files = {
    'json': (None, json.dumps(json_file), 'application/json'),
    'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
}

response = requests.post(url, files=files)

print(response.url)
pprint.pprint(response.text)

#print(response.json())

