import requests
import json


def send_http_request(url):
    r = requests.get(url)
    try:
        print(r.json()['content'])
    except:
        print('Invalid quote resource!')


user_input = input('Input the URL:\n')
send_http_request(user_input)