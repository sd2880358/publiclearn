# 三种方法的案例

class Person:
    #实例方法
    def eat(self):
        print(self)
        print('Eating')
    #类方法
    #类方法的第一个参数,一般命名为cls,区别于self
    @classmethod
    def play(cls):
        print(cls)
        print('Playing')

    #静态方法
    #不需要参数
    @staticmethod

    def say():
        print('saying')

p = Person()
#实例方法
p.eat()
#类方法
Person.play()
p.play()
Person.say()
p.say()