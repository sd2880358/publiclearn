# 7 面象对象的三大特性
- 封装
- 继承
- 多态

## 7.1 封装
- 封装就是对对象的成员进行访问限制
- 封装的三个级别:
    -公开, public
    -受保护的,protected
    -私有的,private
    -public,private,protect 不是关键字
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
- 私有
    - 私有成员是最高级别的封装,只能在当前类或对象中访问
    - 在成员前面添加两个下划线即可
    
            class Person():
                # name是共有的成员
                name = 'Lee'
                #__age就是私有的成员
                __age = 18
    - Python 的私有并不是真私有,是一种通过name mangling的改名策略
    可以使用对象.__classname__attributename访问
- 受保护的对象 protected
    - 受报复的封装是将对象成员进行一定级别的封装,然后,在类中或者子类中部
    可以进行访问,但是外部不可以
    - 封装方法: 在成员名称前添加一个下划线(_)即可
- 公开的, 公共的 public
    - 公开的封装实际成员没有任何操作

## 7.2 继承
- 继承就是一个类可以获得另外一个类中的成员属性和成员方法
- 作用:减少代码(减少重复工作),增加代码的复用功能,同时可以设置类与类直接的关系
- 继承与被继承的概念:
    - 被继承的类叫父类, 也加基类,也叫超类
    - 用于继承的类,叫子类,也叫派生类
    - 继承与被继承一定存在 is-a 关系
    代码表达:
            
            #继承的语法
            #在Python中,任何类都有一个共同的父类:object
            class Person():
                name = "NoName"
                age = 0
                def sleep(self):
                    print("sleepingzzzz)
            #父类写在括号内
            class Teacher (Person)
                pass
                


- 继承的特征
    - 所有的类都继承自object类,即所有的类都是object类的子类
    - 子类一旦继承父类,则可以使用父类中除私有成员外的所有内容
    - 子类继承父类后并有将父类成员完全赋值到子类中,而是通过引用关系访问调用
    - 子类可以定义独有的成员属性和方法
    - 子类中定义的成员和父类的成员如果相同,则优先使用子类的成员
    - 子类如果想扩充父类的方法,可以在定义新方法的同时访问父类的成员来进行代码重用
    可以使用 [父类名,父类成员]的格式来调用父类的成员,也可以使用[super()],父类成员的
    格式来调用 
    #####代码表达
               
            #继承的语法
            #在Python中,任何类都有一个共同的父类:object
            class Person():
                name = "NoName"
                age = 0
                def sleep(self):
                    print("sleepingzzzz)
            #父类写在括号内
            class Teacher (Person)
                teacher_id = '9527'
                name = 'Lee'
                def make_test(self):
                    print("attention")
                def work:
                    #扩充父类的功能只需要调用父类的相应函数
                    #方法1Person.work(self)
                    #方法2super()
                    super().work()
                    self.make_test()
              
- 继承变量函数的查找顺序
    - 优先查找自己的变量
    - 没有则查找父类
    - 构造函数如果本类中没有定义,则自动查找调用父类构造函数
    - 如果本类没有定义,则不再继续向上查找
- 构造函数
    - 是一类特殊的函数,在类进行实例化之前进行调用
    - 如果定义了构造函数,则实例化时使用构造函数,不查找父类的构造函数
    - 如果没定义,则自动查找父类的构造函数
    - 如果子类没定义,父类的构造函数带参数,则构造对象时时的参数应该父类参数构造
    - 在对象进行实例化的时候,系统先自动调入构造函数
    - 构造函数可以通过父类调用进行功能扩展
                
                # X.__init__()
                # super(X, ).__init__(self)
        - 首先调用父类函数,然后执行新增功能
    #####代码表达
            
            class Dog():
            #__init__就是构造函数
            #每次实例化的时候,第一个被调用
            #因为主要工作进行初始化,所以得名
                def __init__(self):
                    print("THIS IS A DOG")
            
            #继承的构造函数
            class Animal:
                pass
            class PaxingAni(Animal)
                pass
            class Dog(PaxingAni):
            #__init__是构造函数
            #每次实例化的时候,第一个被调用
            #因为主要工作进行初始化,所以得名
                def __init__(self):
                    print("THIS IS A DOG")
    
- super 
    - super不是关键字,而是一个类
    - super的作用是获取MRO(MethodResolusionOrder)列表中的第一个类
    - super 与父类没有任何实质性的关系,但是可以通过super来调用父类
    - super使用的两个方法:

- 单继承和多继承
    - 单继承: 每个类只能继承一个类
    - 多继承: 每个类允许继承多个类
    
- 单继承和多继承的优缺点:
    - 单继承:
        - 传承有序逻辑清晰语法简单隐患少
        - 功能不能无限扩展,只能在当前唯一的继承链中扩展
    - 多继承:
        - 优点:类的功能拓展方便
        - 缺点: 继承关系混乱
    代码表达:
        
                class Fish():
                    def __init__(self,name):
                        self.name = name
                    def swim (self):
                        print ("I AM SWIMMING")
                
                class Bird():
                    def __init__(self,name):
                        self.name = name 
                    def fly(self):
                        print("I AM FLYING")
                class Person():
                    def __init__(self,name):
                        self.name = name
                    def work():
                        print("I AM WORKING")
                class Superman (Person, Fish, Bird)
                
- 菱形继承和钻石继承问题:
    - 多个子类继承自同一个父类,这些子类被同一个类继承,于是继承关系图形成一个菱形
    - 关于多继承的MRO
        - MRO就是多继承中,用于保存继承顺序的一个列表
        - Python 本身采用C3算法来自动计算继承算法的结果
        - MRO列表的计算原则:
                       
                        X.__mro__
            - 子类永远在父类前边
            - 如果多个父类,而根据继承语法中括号内类的书写顺序存放
            - 如果多个类继承了同一个父类,孙子类中智慧选取继承语法中扩发中的第一个父类 

## 7.3 多态                   
- 多态是一个对象在不同情况下有不同的状态出现
- 多态不是语法,是一种设计思想
- 多态性:一种调用方式,不同的执行效果
- 多态:同一事物的多种形态, 如:动物分为多种类型

- Mixin设计模式
    - 主要采用多继承方式对类的功能进行扩展
    - 优点
        - 使用Mixin可以在不对类进行任何修改的情况下,扩充功能
        - 可以方便的组织和维护不同功能组件的划分
        - 可以根据需要调整功能类的组合
        - 可以避免创建很多新的类,不会导致类的继承混乱
- 使用多继承语法来实现Mixin
    - 使用Mixin实现多继承的时候需要非常小心
    - 首先职责必须表示单一功能,而不是某个物品
    - Mixin不能依赖于子类的实现
    - 子类没有继承这个Mixin类
代码表现:
                
    - 多继承表达    
                      
          class person(): 
            name = 'Lee'
            age = 18
            
            def eat(self):
                print('eat')
            def drink(self):
                print('drink')
            def sleep(self):
                print('sleep)
            
            
          class Teacher(person):
            def work(self):
                print('work')
                
          class Student(person):
            def study(self):
                print('study')
                
          class Tutor(Teacher,Student)
            pass 
            
    - Mixin表达
    
          
          class TeacherMixin():
            def work(self):
                print('work')
                
          class StudentMixin():
            def study(self):
                print('study')
                
          class TutorM(person,TeacherMixin,StudentMixin)
            pass

# 8 类相关函数
- issubclass(X,Y) :检测是否为子集
- isinstance(X,Y): 检测一个对象是否是一个对象的实例
- hasattr(X,Y):检测一个对象是否是一个类成员
- getattr:
- setattr:
- delattr:
- dir: 获取对象的成员列表