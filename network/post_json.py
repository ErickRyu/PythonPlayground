import json
import requests, pprint

url = 'https://miffle.braydenlab.com/miffle/file_get_json.php'
#headers = {'content-type': 'application/json'}

f = open('train_condition.json', 'r')
json_file = json.load(f)

response = requests.post(url, data=json.dumps(json_file))

pprint.pprint(response.text)
