'''
利用request 下载网页,自动检测页面

'''

import urllib
import chardet

if __name__ == '__main__':
    url = 'http://mcar.cc/search.php?mod=forum'

    rsp = urllib.request.urlopen(url)


    html = rsp.read()
    cs = chardet.detect(html)
    print(cs)
    print(type(cs))

    html = html.decode(cs.get('encoding','utf-8'))

    print(html)

