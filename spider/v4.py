'''
利用request 下载网页,自动检测页面

'''

from urllib import request,parse


if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    wd = input('input your keyword')

    qs = {
        "wd":wd
    }
    qs = parse.urlencode(qs)

    rsp = request.urlopen(url)

    fullurl = url + qs
    print(type(qs))

    print(fullurl)

    html = request.urlopen(fullurl)


    html = rsp.read()

    html = html.decode()

    print(html)
    # html = html.decode(cs.get('encoding','utf-8'))
    #
    # print(html)

