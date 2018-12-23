'''
使用代理访问百度网站
'''

from urllib import request, error

if __name__ == '__main__':

    url = 'http://www.baidu.com'

    proxy = {'http://':'183.89.203.90:8080'}


    proxy_handler = request.ProxyHandler(proxy)

    opener = request.build_opener(proxy_handler)

    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
