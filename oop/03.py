class A():
    def __init__(self,name = 0):
        print('hahaha')

    def __call__(self):
        print('haha,i been call again')

    def __str__(self):
        return "Lee"
    def __getattr__(self, item):
        pass
        #print('There is none')
        #print(item)
a = A()
a()

print(a.addr)


#__setattr__案例

class People():
    def __init__(self):
        pass
    def __setattr__(self,name,value):
        print('设置属性:{0}'.format(name))
        #self.name = value
        #为了避免此种情况,死循环,规定统一调用父类函数的魔法函数
        super().__setattr__(self,name)

p = People
p.age = 18