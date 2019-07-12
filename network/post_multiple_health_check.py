import json
import requests
import threading
import time
import random

# url = 'https://miffle.braydenlab.com/miffle/file_get_multiple.php'
# url = 'https://miffle.braydenlab.com/miffle/post_php.php'
# url = 'https://miffle.braydenlab.com/miffle/get_files_and_calc.php'
#url = 'https://toffle.braydenlab.com/leuven/post_php.php'
#url = 'https://general.braydenlab.com/service/post_php.php'
#url = 'https://general.braydenlab.com/port/cpr_test'
#url = 'https://general.braydenlab.com/port/sample'
#url = 'https://general.braydenlab.com/service/cpr_testout.php'

#url ='http://general.braydenlab.com/port/cpr_analyzer_provider_genk'
WEIGHT_THRESHOLD = 0.7
url =[
    'https://seoul1.braydenonline.cc/port/health_check',
    'https://seoul4.braydenonline.cc/port/health_check',
    'https://seoul5.braydenonline.cc/port/health_check',
    'https://ohio.braydenonline.cc/port/health_check'
    ]
#url ='http://52.79.213.249/port/cpr_analyzer_provider_genk'
#url2 ='http://13.125.87.4/port/cpr_analyzer_provider_genk'

#url ='https://hstream.braydenlab.com/hstream/cpr_analyze_provider.php'
#url ='https://miffle.braydenlab.com/port/cpr_analyzer_provider_leuven'

rawHexBPfile = 'bigsize_rawHexBPfile.bin'
TMP_ACCESS_TOKEN = 'AUctDh9v6OKpNHlnwcC94Q=='
MILLI_SEC = 1000
WEIGHT_STANDARD = 10

list_resp_instance = list()


# 일정시간 이내에 이 쓰레드는 끝날 것이라고 가정한다.
def post_thread(url):
    try:
        start_time = time.time()
        response = requests.get(url, headers={'AccessToken': TMP_ACCESS_TOKEN})
        end_time = time.time()

        response_text = response.text
        print(response.url)
        print(response_text)

        result = {
            'url': url,
            'resp_time': (end_time - start_time) * MILLI_SEC,
            'weight_value': 0
         }
        result.update(json.loads(response_text))

        list_resp_instance.append(result)

        print(list_resp_instance)
    except Exception as e:
        print(e)


def pick_server_using_weight():
    calculate_weight()
    sorted_list = sorted(list_resp_instance, key=lambda obj: obj['weight'])
    highest_weight_value = sorted_list[0]['weight']

    index_to_start_pop = 0
    for _ in list_resp_instance:
        if highest_weight_value * WEIGHT_THRESHOLD > sorted_list[index_to_start_pop]['weight']:
            break
        index_to_start_pop += 1

    del(sorted_list[index_to_start_pop:])
    print(sorted_list)

    return sorted_list[random.randrange(len(sorted_list))]['url']


def calculate_weight():
    resp_time_standard = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
    free_storage_standard = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05]
    for obj in list_resp_instance:
        resp_time = obj['resp_time']
        free_percentage = obj['GB_free'] / obj['GB_total']
        weight = 10
        for i in range(10):
            if resp_time < resp_time_standard[i]:
                weight = WEIGHT_STANDARD - i
                break
        obj['resp_weight'] = weight
        for i in range(10):
            if free_percentage > free_storage_standard[i]:
                weight = WEIGHT_STANDARD - i
                break;
        obj['storage_weight'] = weight

        obj['weight'] = min(obj['resp_weight'], obj['storage_weight'])


if __name__ == "__main__":
    xSend = []

    for i in range(len(url)):
        xSend.append(threading.Thread(target=post_thread, args=(url[i], )))

    print('Start thread')
    for i in range(len(url)):
        xSend[i].start()

    for i in range(len(url)):
        xSend[i].join()

    url_to_connect = pick_server_using_weight()
    if url_to_connect == '':
        print('can\'t connect to server')
    else:
        print('url to connect : ', url_to_connect)
