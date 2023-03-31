import requests


def is_scrapable(url):
    response = requests.get(url)
    status_code = str(response.status_code)
    return not (status_code[0]=='4' or status_code[0]=='5')
