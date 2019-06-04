import re
import argparse
import json
import requests
import time

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

    start_time = time.time()
    response = requests.post(args['url'], files=files)
    elapsed_time = time.time() - start_time

    result = dict()
    if response.status_code == 500:
        print('500 error')
        result = {'Error': ['Service is not responding']}
    else:
        print('No 500 error', response.status_code)
        result = json.loads(response.text)

    report_json = dict()
    if 'SystemReport' in result:
        report_json = result['SystemReport']
    else:
        report_json = result

    report_json['response_time'] = elapsed_time
    report_file = open(domain_header + '_report.json', 'w')
    report_file.write(json.dumps(report_json))
    report_file.close()
