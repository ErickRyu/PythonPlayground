import json
import requests
import threading
import time

global status_response
status_response = 'idle'
content_response = ''


def is_usage_in_result(content):
    if content == '':
        return False
    elif 'Usage' in json.loads(content):
        print("Expected value")
        return True
    return False


def post_thread(case_number):

    url = 'https://hstream.braydenlab.com/hstream/cpr_analyze_provider.php'
    f_json = open('normal_train_condition.json', 'rb')
    #f_bin = open('bigsize_rawHexBPfile.bin', 'rb')
    f_bin = open('zerosize.bin', 'rb')

    json_file = json.load(f_json)
    if case_number == 0:
        json_file['Debug']['Force_Error'] = 'empty_open_skills'
    elif case_number == 1:
        json_file['Debug']['Force_Error'] = 'empty_hex_content'
    elif case_number == 2:
        json_file['Debug']['Force_Error'] = 'unexpected_termination'

    files = {
        'data': (None, json.dumps(json_file), 'application/json'),
        'rawHexBPfile': ('rawHexBPfile.bin', f_bin, 'application/octet-stream')
    }
    response = requests.post(url, files=files)
    global content_response
    content_response = response.text
    if is_usage_in_result(content_response):
        global status_response
        status_response = 'complete'


if __name__ == "__main__":

    start_time = time.time()

    for repeat in range(0, 4):

        if status_response == 'complete':
            continue

        xSend = threading.Thread(target=post_thread, args=(repeat,))
        print('Run thread #', repeat)
        xSend.start()

        for waitingDly_100ms in range(0, 60):
            if status_response == 'complete':
                continue
            time.sleep(0.1)

    for maxDly_100ms in range(0, 100):
        if status_response == 'complete':
            continue
        time.sleep(0.1)

    if status_response == 'complete':
        print('Get the result successfully')
        status_response = 'idle'
    elif status_response == 'idle':
        status_response = 'Fail'
        print('Failed')

    elapsed_time = time.time() - start_time
    print('Elapsed time: ', elapsed_time, 'sec')