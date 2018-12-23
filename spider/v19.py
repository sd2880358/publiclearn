
from urllib import request
import json
a = 20
d = list()
for i in range(5):

    url = ('https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&' + 'start=' + str(a) + '&limit=20')

    rsp = request.urlopen(url)

    data = rsp.read().decode()

    data = json.loads(data)


    a += 20
    d += (data)

print (d)