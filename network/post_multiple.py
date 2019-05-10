import json
import requests
import time

# url = 'https://miffle.braydenlab.com/miffle/file_get_multiple.php'
# url = 'https://miffle.braydenlab.com/miffle/post_php.php'
# url = 'https://miffle.braydenlab.com/miffle/get_files_and_calc.php'
#url = 'https://toffle.braydenlab.com/leuven/post_php.php'
#url = 'https://general.braydenlab.com/service/post_php.php'
#url = 'https://general.braydenlab.com/port/cpr_test'
#url = 'https://general.braydenlab.com/port/sample'
#url = 'https://general.braydenlab.com/service/cpr_testout.php'
#url ='https://general.braydenlab.com/port/cpr_analyzer_provider_genk'
url ='https://hstream.braydenlab.com/hstream/cpr_analyze_provider.php'

rawHexBPfile = 'bigsize_rawHexBPfile.bin'

#f_json = open('bigsize_train_condition.json', 'rb')
#f_bin = open('bigsize_rawHexBPfile.bin', 'rb')
# f_json = open('normal_train_condition.json', 'rb')
# f_bin = open('normal_rawHexBPfile.bin', 'rb')

f_json = open('normal_train_condition.json', 'rb')
f_bin = open(rawHexBPfile, 'rb')
json_file = json.load(f_json)
files = {
    'data': (None, json.dumps(json_file), 'application/json'),
    'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
}

response = requests.post(url, files=files)
print(response.url)
print(response.text)
# time.sleep(0.1)

f_bin = open(rawHexBPfile, 'rb')
files = {
    'data': (None, json.dumps(json_file), 'application/json'),
    'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
}

response = requests.post(url, files=files)
print(response.url)
print(response.text)

if response.text == '':
    print('--------------- None response --------------')

    f_bin = open(rawHexBPfile, 'rb')
    files = {
        'data': (None, json.dumps(json_file), 'application/json'),
        'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
    }

    response = requests.post(url, files=files)
    print(response.url)
    print(response.text)

# f_bin = open(rawHexBPfile, 'rb')
# files = {
#     'data': (None, json.dumps(json_file), 'application/json'),
#     'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
# }
#
# response = requests.post(url, files=files)
# print(response.url)
# print(response.text)
