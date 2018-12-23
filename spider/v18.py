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

    md5.update(v, encoding='utf-8')

    sign = md5.hexdigest()

    return sign
