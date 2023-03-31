import requests


def is_scrapable(url):
    response=requests.get(url)
    return response.status_code

