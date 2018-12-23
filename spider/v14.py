from urllib import request, parse

from http import cookiejar


filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)

cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    url = 'http://passport.zhan.com/UsersLogin/login.html?url=http%3A%2F%2Fi.zhan.com%2F'

    data = {
        'username':'18077691998',
        'pwd':'73143177da'
    }

    data = parse.urlencode(data)

    req = request.Request(url, data=data.encode())

    rsp = opener.open(req)

    html = rsp.read().decode()
    cookie.save(filename,ignore_expires=True,ignore_discard=True)

    cookie.save(ignore_discard=True, ignore_expires=True)
def getHomepage():
    url = 'http://i.zhan.com/'
    rsp = opener.open(url)
    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    login()
    getHomepage()
