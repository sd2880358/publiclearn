'''
利用parse模块模拟post请求
分析百度词典
分析步骤:
请求地址是http://fanyi.baidu.com/sug
查看sug值发现是KW:girl
检查返回内容,发现返回的事json格式内容,需要使用json包
'''

from urllib import request, parse
import json
'''
大致流程:
1. 利用data 构造内容,然后url打开
2. 返回一个json格式的结果
3. 结果就应该是一个girl的
'''

base_url = 'https://fanyi.baidu.com/sug'
# 存储模拟数据
a = input('查询单词')
data = {
    'kw': a
}
data = parse.urlencode(data).encode()

print(type(data))
# 构造请求头
# request 要求传入的请求头是一个dict格式

rsp = request.urlopen(base_url, data=data)
json_data = rsp.read().decode('utf-8')
# print(json_data)
json_data = json.loads(json_data)
# print(json_data)

for item in json_data['data']:
    print(item['k'],'--',item['v'])