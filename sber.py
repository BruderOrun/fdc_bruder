import requests
import datetime
import re


def sber_dates_published_reports(url):
    year = str(datetime.datetime.now().year)[2::]
    response = requests.get(url)
    pattern = re.compile('\w102\S*\w*\S*' + year + '.zip')
    return str(pattern.findall(response.text))
