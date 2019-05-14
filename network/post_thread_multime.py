import json
import requests
import threading
import time


status_response = 'idle'
content_response = ''

def post_thread():
    url = 'https://hstream.braydenlab.com/hstream/cpr_analyze_provider.php'
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
    global content_response
    content_response = response.text


if __name__ == "__main__":

    for repeat in range(0, 3):
        if status_response == 'complete':
            continue

        xSend = threading.Thread(target=post_thread, args=())
        print('Start thread')
        xSend.start()

        for waitingDly in range(0, 400):
            if status_response == 'complete':
                continue
            time.sleep(0.1)

