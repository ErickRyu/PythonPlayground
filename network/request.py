import requests, pprint

url = 'https://miffle.braydenlab.com/miffle/post_php.php'
headers = {
    'Content-type': 'multipart/form-data'
}
json_file = open('train_condition.json', 'r')
rawH_file = open('rawHexBPfile.bin', 'rb')

files = {'rawHexBPfil.bin':rawH_file}
response = requests.post(url, files=files, data=json_file.read(), headers=headers)

pprint.pprint(response.text)
