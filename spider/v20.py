import requests

url = 'http://www.baidu.com'
rsp = requests.get(url)
rsp = requests.request('get',url)
print(rsp.text)
