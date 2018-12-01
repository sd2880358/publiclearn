class A():
    def __init__(self):
        self.name = 'haha'
        self.age = 18

    #此功能是对变量进行读取操作
    def fget(self):
        print('It was read')
        return self.name
    # 模拟的事对变量进行的鞋操作
    def fset(self,name):
        print('我被写入了')
        self.name = 'lee' + name

    #模拟删除进行的操作
    def fdel(self):
        pass

    #property 的四个顺序是固定的(fget,fset,fdel,doc说明文档)
    name2 = property(fget,fset,fdel,'这是一个property的例子')

a = A()
print (a.name)

print(a.name2)

a.name2 = 'Lee'