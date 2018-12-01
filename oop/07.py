#抽象类实现

import abc
#声明一个类并且指定当前类的元类
class Huam(metaclassabc.ABCMeta)

    # 定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass
    #定义类抽象方法
    @abc.abstractmethod
    def drink ():
        pass
    # 定义静态抽象方法
    @abc.abstractmethod
    def play():
        pass

