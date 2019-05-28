import sys
import json
import requests

url ='https://hstream.braydenlab.com/hstream/cpr_analyze_provider.php'

rawHexBPfile = 'normal_rawHexBPfile.bin'


if __name__ == "__main__":

    print(sys.argv[0])
    f_json = open('normal_train_condition.json', 'rb')
    f_bin = open(rawHexBPfile, 'rb')

    json_file = json.load(f_json)
    files = {
        'data': (None, json.dumps(json_file), 'application/json'),
        'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
    }

    response = requests.post(url, files=files)
    print(response.text)

    result = json.loads(response.text)

    print(result['SystemReport'])
