#自己组装类

class A():
    pass

def say(self):
    print('saying')

say(9)

A.say = say

a = A()

a.say()

#组装类的例子1

from types import MethodType

class A():
    pass

def say(self):
    print('saying')

a = A()
a.say = MethodType(say,A)
a.say()

# 使用type造一个类

# 先定义类应该具有的成员函数
def say (self):
    print('saying')
def talk(self):
    print('talking')

#用type创建一个类

A = type('aName',(object,),{'class_say':say,'class_talk':talk})

a = A()

a.class_say()

# 元类演示

#元类的写法是固定的,ta必须继承字type
#元类的写法一般命名为MateClass
class TulingMetaClass(type):
    #注意一下写法
    def __new__(cls,name,bases,attrs):
    #自己的业务处理
        print('haha,I\'m a tuple')
        attrs['id'] = '0000'
        attrs['addr'] = 'guess'
        return type.__new__(cls,name,bases,attrs)
#元类定义完后就可以使用,使用注意写法

class Teacher(object,metaclass=TulingMetaClass):
    pass

t = Teacher

