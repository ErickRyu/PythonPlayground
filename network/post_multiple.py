import json
import requests, pprint

# url = 'https://miffle.braydenlab.com/miffle/file_get_multiple.php'
# url = 'https://miffle.braydenlab.com/miffle/post_php.php'
# url = 'https://miffle.braydenlab.com/miffle/get_files_and_calc.php'
#url = 'https://toffle.braydenlab.com/leuven/post_php.php'
#url = 'https://general.braydenlab.com/service/post_php.php'
#url = 'https://general.braydenlab.com/port/cpr_test'
#url = 'https://general.braydenlab.com/port/sample'
#url = 'https://general.braydenlab.com/service/cpr_testout.php'
url ='https://general.braydenlab.com/port/cpr_analyzer_provider_genk'

f_json = open('train_condition.json', 'rb')
f_bin = open('rawHexBPfile.bin', 'rb')

json_file = json.load(f_json)
files = {
    'data': (None, json.dumps(json_file), 'application/json'),
    'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
}

response = requests.post(url, files=files)

print(response.url)
#pprint.pprint(response.text)
print(response.text)