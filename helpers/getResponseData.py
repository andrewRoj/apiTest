import json


def response_data(response):
    if response.ok:
        data = json.loads(response.text)
        return data
    else:
        print(response.status_code)
