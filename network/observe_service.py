import re
import argparse
import json
import requests

'''
Usage example: 
python observe_service.py -u https://hstream.braydenlab.com/hstream/cpr_analyze_provider.php
python observe_service.py -u https://general.braydenlab.com/port/cpr_analyzer_provider_genk
'''
prefix = 'normal'
rawHexBPfile = prefix + '_rawHexBPfile.bin'


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--url', type=str, default='', help='input URL to request')
    args = vars(parser.parse_args())

    domain_header = re.findall('//([^.]*)', args['url'])[0]

    f_json = open(prefix + '_train_condition.json', 'rb')
    f_bin = open(rawHexBPfile, 'rb')

    json_file = json.load(f_json)
    files = {
        'data': (None, json.dumps(json_file), 'application/json'),
        'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
    }

    response = requests.post(args['url'], files=files)
    result = json.loads(response.text)

    report_json = result
    if 'SystemReport' in result:
        print(result['SystemReport'])
        report_json = result['SystemReport']

    report_file = open(domain_header + '_report.json', 'w')
    report_file.write(json.dumps(report_json))
    report_file.close()
