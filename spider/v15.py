from urllib import request, parse

from http import cookiejar

cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)




cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler,https_handler,cookie_handler)


def getHomepage():
    url = 'http://i.zhan.com/'
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open('rsp.html','w') as f:
        f.write(html)
if __name__ == '__main__':
    getHomepage()