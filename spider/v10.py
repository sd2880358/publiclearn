from urllib import request
if __name__ == '__main__':
    url = 'http://www.renren.com/969196280/profile'

    rsp = request.urlopen(url)

    html = rsp.read().decode()
    with open('rsp.html','w') as f:
        f.write(html)