# __gt__

class Student():
    def __init__(self,name):
            self._name = name

    def __gt__(self,obj):
        print('哈哈,{0}会比{1}大吗?'.format(self.obj))
        return self._name > obj._name

stu1 = Student('one')
stu2 = Student('two')
