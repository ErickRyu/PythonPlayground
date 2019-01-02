import requests
import json

url = 'https://miffle.braydenlab.com/miffle/simple_get.php'
payload = {"device":"gabriel","data_type":"data","zone":1,"sample":4,"count":0,"time_stamp":"00:00"}
headers = {'content-type': 'application/json'}

f = open('train_condition.json', 'r')
json_file = json.load(f)

#response = requests.post(url, data=json.dumps(payload), headers=headers)
response = requests.post(url, data=json.dumps(json_file), headers=headers)

print(response.text)