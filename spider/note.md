# 0 爬虫准备工作
- 参考资料
    - python网络数据采集,图灵工业出版
    - 精通python爬虫构架Scrapy,人民邮电出版社
    - python3网络爬虫
    - Scrapy官方教程

- 前提知识:
    -URL
    -http协议
    -web前端内容
    -ajax
    -re,xpath
    -xml
    
# 1. 爬虫简介
- 爬虫定义: google
- 两大特征:
    - 能按作者的要求来下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤:
    - 下载网页
    - 提取正确的信息
    - 根据一定的规则自动跳转到另外的网页上,执行上下两部内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫(聚焦爬虫)
- Python网络包简介
```
Python 3.x: urllib, urlib3, httplib2, requests

```

## 2.urllib
- 包含模块
    - urllib.request: 打开和读取urls
    - urllib.error: 包含urllib.request产生的常见的错误,使用try捕捉
    - urllib.parse: 包含解析url的方法
    - urllib.robotparse: 解析robot.txt文件
    案例01
- 网络编码问题解决
    - chardet 可以自动检测页面文件的编码格式, 但是,有可能有误
    - 需要安装
    - 案例v02
- urlopen 的返回对象
    - 案例v3
    - geturl :返回请求对象的url
    - info: 请求反馈对象的meta信息
    - getcode:返回code信息
- request.date的使用
    - 访问网络的两种方法
        - get
            - 利用参数给服务器传递信息
            - 参数为dict, 然后用parse编码
            - 案例v4
        - post
            - 一般向服务器传递参数使用
            - post 是把信息自动加密处理
            - 我们如果想使用post信息,需要给date参数
            - 使用post,意味着http的请求头可能需要更改:
                - content-type: application/x-www.from-url-urlencode
                - content-length: 请求数据长度
                - 简而言之, 一旦更改请求方法,请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面
            - 案例05
            - 为了更多的设置请求信息,单纯通过urlopen函数已经不太好用了
            - 需要利用request.Request 类
            - 案例v6

- urllib.error
    - URLError 产生的原因:
        - 没有网络
        - 服务器连接失败
        - 找不到指定的服务器
        - 是OSError的子类   
    - HTTPError, 是URLError的一个子类       
    - 两者区别:
        - HTTPError是对应的HTTP请求的返回码错误,如果返回错误是400以上,则引发HTTPError
        - URLError对应一般是网络的问题,包括URL问题     
    - 案例v7
    
- UserAgent
    - UserAgent: 用户代理,简称UA,属于heads的一部分,服务器通过UA来判断访问者的身份
    - 常见的UA的值,使用的时候可以直接复制粘贴,也可以用浏览器访问的时候抓包
    ```
    chrome 
    Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 
    Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11 
    Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16

    Firefox 
    Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0 
    Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10

    Opera 
    Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60 
    Opera/8.0 (Windows NT 5.1; U; en) 
    Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50 
    Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50

    IPhone 
    Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9(KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5
 
    Android 
    Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
    Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    
    ```
    - 设置UA可以通过两种方法:
    - heads
    - add_header
    - 案例v8
- ProxyHandler处理(代理服务器)
    - 使用代理IP, 是爬虫常用手段
    - 获取代理服务器的地址:
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来伪装请求者的真实ip地址
    - 基本使用步骤:
        1. 设置代理地址
        2. 创建ProxyHandler
        3. 创建Opener
        4. 安装Opener
        案例v9
- cookie & session
    - 由于http协议无记忆性,人们为了弥补这个问题,所采用的一个补充协议
    - cookie 是发放给用户(即http浏览器)的一段信息,session是保存在服务器上的对应的另一半信息,用来记录用户信息
    
- cookie和session的区别
    - 存放位置不同
    - cookie不安全
    - session会保存在服务器上, 一定时间会自动清空
- session的存放位置
    - 存在服务器端
    - 一般情况, session是放在内存中或者服务器的数据库中
    - 没有cookie登录 v10
    - 手动挂上cookie登录, v11
        - 直接把cookie复制下来,然后手动放入请求头, 案例v11
    - HTTP模块包含一些关于cookie模块,通过他们我们可以自动使用cookie
        - CookieJar
            - 管理存储Cookie, 向传出的HTTP请求添加Cookie
            - Cookie存储在内存中,Cookie实例后回收cookie将消失
        - FileCookieJar(filename, delayload=0, policy=0):
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar(filename, delayload=0, policy=0):
            - 创建mozilla浏览器cookie.txt兼容的FileCookieJar实例
        - LwpCookieJar(filename, delayload=0, policy=0):
            - 创建libwww.perl标准兼容的set-Cookie3格式的fileCookieJar实例
        - 他们的关系是: CookieJar --> FileCookieJar --> MozillaCookieJar & LwpCookieJar
        - 利用cookieJar访问人人 案v12
            - 流程:
                - 打开登录页面后自动通过用户名登录
                - 自动提取反馈回来的cookie
                - 利用提取的cookie登录隐私页面
            - handler是Handler的实例, 常用的有
            - 用来处理复杂请求
            ```
            cookie_handler = request.HTTPCookieProcessor(cookie)
            http_handler = request.HTTPHandler()
            https_handler = request.HTTPSHandler()
            ```
        - 创建handler后,使用opener打开, 打开后相应的功能由相应的handler处理
        - cookie作为一个变量,打印出来案例 v13
            - cookie的属性
                - name:名称
                - value: 值
                - domain: 可以访问此cookie的域名
                - path: 可以访问cookie的页面路径
                - expires: 过期时间
                - size: 大小
                - http字段
        - cookie的保存 - FileCookieJar 案例14
        - cookie的读取 案例15

## SSL
> SSL证书就是遵守SSL安全套阶层协议的服务器数字整数(SecureSocketLayer)  
由美国网景公司开发  
CA (CertificateAuthority)是数字证书认证中心,是发放,管理,废除数字证书的收信人的第三方机构  
遇到不信任的SSL证书,需要单独处理,案例v16

## JS加密
- 有的反爬虫策略采用js对需要传输的数据进行加密处理(通常是取md5值)
> 经过加密,传输的就是密文,*但是*加密函数或者过程一定是在浏览器完成,也就是一定会把代码(js代码)暴露给使用者  
通过阅读加密算法,就可以模拟出加密的过程,从而达到破解  
- 参看案例v17,v18

## ajax
- 异步请求
- 一定会有url, 请求方法,可能有数据
- 一般使用json格式
- 案例, 爬取豆瓣电影,v19

# Requests - 献给人类
- HTTP for Humans, 更简洁,更友好
- 继承了urllib的所有特征
- 开源地址: GitHub
- get请求
    - requests.get()
    - requests.request('get',url)
    - 可以带有headers 和parmas参数
    - 案例v20
- get 返回内容
    - 案例v21
-post 
    -rsp = requests.post(url, data=data)
    - 案例22
- proxy
    - proxies={}
    - requests.request('get', url, proxy=proxies)
    - 代理有可能会报错,如果使用人数多,考虑安全,可能会被强行关闭
- 用户验证
    - 代理验证
        ```
        # 可能需要使用HTTP basic Auth 可以这样
        # 格式为 用户名:密码加@代理地址:端口地址   
        proxies = {'http':'China:123456@192.169.1.123:444'}
        rsp = requests.get('http://baidu.com',proxies=proxy)
        ```
- web客户端验证
    - 如果遇到web客户端验证,需要添加auth=(用户名,密码)
    auth=('test1','123456')#授权信息
    rsq = requests.get('http://www.baidu.com', auth=auth)
- cookie
> 通过requests可以自动处理cookie信息  

```
rsp = request.get(url)
#如果对方服务器给传送过来cookie信息,则可以通过反馈得到cookie的属性
cookiejar = rsp.cookies
可以将cookieJar转换成字典
cookiedict = request.utils.dic_from_cookiejar(cookiejar)
```

- session
    - 跟服务器端的session不是一个东西
    - 模拟一次会话, 从客户端浏览器连接服务器开始,到客户端浏览器断开.
    - 能让我们跨请求时保持某些参数,比如在同一个session实例发出的所有请求之间保持cookie
    ```
    ss = request.session()
    
    headers = {'User-Agent':'xxx'}
    data = {'name':'xx'}
    # 此时,发出请求用session管理请求,则由创建的session管理请求
    ss.post('http://www.baidu.com,data=data,headers=headers)
    rsp = ss.get('')
    ```
- https请求验证ssl证书
    - 如果需要验证, 参数verify负责表示是否验证ssl证书, 默认True
    - 如果不需要验证ssl证书,则设置成false表示关闭