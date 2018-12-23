from urllib import request, parse

from http import cookiejar



cookie = cookiejar.CookieJar()

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
    with open('test.html','w') as f:
        f.write(html)

def getHomepage():
    url = 'http://i.zhan.com/'
    rsp = opener.open(url)
    html = rsp.read().decode()

if __name__ == '__main__':
    login()
    print(cookie)
    for item in cookie:
        print(item)
        print(type(item))
        for i in dir(item):
            print(i)
    getHomepage()