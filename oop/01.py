'''
定义一个学生的类,用来形容学生
'''

class Student():
    # 一个空类, pass代表直接跳过
    # 此处必须有pass
    pass


# 定义一个对象
Lee = Student()

# 再定义一个类, 用来描述挺Python的学生
class PythonStudent():
    # 用None 给不明确的值赋值
    name = None
    age = 18
    course = "Python"

    '''
    需要注意
    1. def 的缩进层级
    2. 系统默认由一个self参数
    '''
    def doHomework(self):
        print ("I am doing homework")

        return None

#实例化一个叫yueyue的学生,是一个具体的人
yueyue = PythonStudent()
print (yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传入函数
yueyue.doHomework()

