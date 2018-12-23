from urllib import request

if __name__ == '__main__':
    url = 'http://i.zhan.com/'
    header = {
        'Cookie':'_csrf=b2caaee278a5c2cbd471221321193615e74caee0cdea420e267791d4a688c5d8a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22py_rvBEEu7qjBzHllLtLbYcvyGhGJ8fm%22%3B%7D'
    }

    rqs = request.Request(url, headers=header)

    rps = request.urlopen(rqs)

    html = rps.read().decode()
    print(html)

    with open('rspWithCookie1.html','w') as f:
        f.write(html)