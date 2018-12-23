import requests

url = 'http://www.baidu.com/s?'

kw = {'kw':'王八蛋'}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0 '
}
rsp = requests.get(url, params=kw, headers=headers)

print(rsp.text)

print(rsp.content)

print(rsp.url)