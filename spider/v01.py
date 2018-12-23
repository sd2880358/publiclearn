'''
使用urllib.request请求一个网页内容,并把内容打印出来
'''

from urllib import request

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    # 打开url并把相应的页面作为返回
    rsp = request.urlopen(url)
    #把返回结果读取出来
    http = rsp.read()

    print(http.decode())