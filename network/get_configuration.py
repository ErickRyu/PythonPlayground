import requests
import json
import pprint

url ='https://general.braydenlab.com/port/registration'


if __name__ == "__main__":
    response = requests.post(url, data={'clientid': 'oost-limburg', 'passcode': '011235'})
    print(json.loads(response.text))