import json
import requests
import threading
import time


def post_thread():
    url = 'https://general.braydenlab.com/port/cpr_analyzer_provider_genk'
    # url = 'https://hstream.braydenlab.com/hstream/cpr_analyze_provider.php'
    f_json = open('normal_train_condition.json', 'rb')
    f_bin = open('bigsize_rawHexBPfile.bin', 'rb')

    json_file = json.load(f_json)
    files = {
        'data': (None, json.dumps(json_file), 'application/json'),
        'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
    }
    response = requests.post(url, files=files)
    print(response.url)
    print(response.text)


if __name__ == "__main__":

    xSend = threading.Thread(target=post_thread, args=())
    print('Start thread')
    xSend.start()

    xSend = threading.Thread(target=post_thread, args=())
    print('Start thread')
    xSend.start()

    xSend = threading.Thread(target=post_thread, args=())
    print('Start thread')
    xSend.start()
