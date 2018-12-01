#属性案例
#创建Student类,描述学生类
#学生具有Student.name属性
#但name格式并不同意

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print('Hi, my name is {0}'.format(self.name))

    def setName(self,name):
        self.name = name.upper()
    def setName(self,age):
        self.age = int(age)


s1 = Student('Lee',19)
s2 = Student('michi stangle',24)

s1.intro()
s2.intro()

print('*'*20)

# property 案例
# 定义一个person类,具有name,age属性
# 对于任意输入的姓名,我们希望都用大写来保存
# 年龄, 我们希望内部统一用整数保存
# x = property(fget,fset,fdel,doc)

class person():
    #函数的名称任意
    def fget(self):
        return self._name*2
    def fset (self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = "Noname"

    name = property(fget,fset,fdel,"对Name进行以下操作")
p1 = person()
p1.name = 'Lee'
print(p1.name)