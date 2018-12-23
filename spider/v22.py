import requests

url = 'https://fanyi.baidu.com/sug'

data = {

    'kw':'girl'
}


header = {
    'Content-Length': str(len(data))
}

rsp = requests.post(url, data=data,headers= header)

print(rsp.text)
print(rsp.json())