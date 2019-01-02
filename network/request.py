import json
import requests, pprint

url = 'https://miffle.braydenlab.com/miffle/post_test.php'
#headers = {    'Content-type': 'multipart/form-data'}
headers = {'content-type': 'application/json'}

f = open('train_condition.json', 'r')
json_file = json.load(f)

rawH_file = open('rawHexBPfile.bin', 'rb')

files = {'rawHexBPfil.bin':rawH_file}
#response = requests.post(url, data=json.dumps(json_file), files=files, headers=headers)
response = requests.post(url, data=json.dumps(json_file), headers=headers)

pprint.pprint(response.text)
