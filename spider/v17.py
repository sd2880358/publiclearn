
from urllib import request, parse
from urllib import request, parse
import time
import random
'''
r = "" + (new Date).getTime(),
i = r + parseInt(10 * Math.random(), 10)
sign: n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
md5 一共需要四个参数,第一个和第四个都是字符串,
'''


def getSalt():
    r = int(time.time()*1000)
    i = r + random.randint(0,10)
    salt = i
    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()

    md5.update(v.encode('utf-8'))

    sign = md5.hexdigest()

    return sign
def getSign(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
    sign = getMD5(sign)
    return sign



def youdao(key):
        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        salt = getSalt()
        data = {'i': key,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': getSign(key,salt),
            'ts': int(time.time()*1000),
            'bv': getMD5(key),
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'ypoResult': 'false'}
        data = parse.urlencode(data).encode()

        header = {'Accept': 'application/json, text/javascript, */*;q=0.01',
                #'Accept-Encoding':'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9, zh-CN;q=0.8,zh;q=0.7',
                'Connection': 'keep - alive',
                'Content-Length': len(data),
                'Content-Type': "application/x-www-form-urlencoded;charset' = UTF-8",
                'Cookie': "OUTFOX_SEARCH_USER_ID = 813253043@108.7.201.143;OUTFOX_SEARCH_USER_ID_NCOO = 16857097.056581017;_ntes_nnid=902fc284f2189e4b7231583a68d1b792,1543516185959; DICT_UGC = be3af0da19b5c5e6aa4e17bd8d90b28a|;JSESSIONID = abcm1bxzCdwP9 - xtBQVEw;___rl__test__cookies = 1545446687330",
                'Host': "fanyi.youdao.com",
                'Origin': "http://fanyi.youdao.com",
                'Referer': 'http://fanyi.youdao.com /?keyfrom = dict2.index',
                'User-Agent': "Mozilla/5.0(Macintosh;IntelMac OSX10_13_6) AppleWebKit/537.36(KHTML, like Gecko)Chrome/71.0.3578.98Safari/537.36",
                'X-Requested-With': 'XMLHttpRequest'
       }

        req = request.Request(url=url, data=data, headers=header)
        rsp = request.urlopen(req)

        html = rsp.read().decode()

        print(html)

if __name__ == '__main__':
    youdao('lady')
