- 邮箱
    - 用python发送邮件
    - 对邮箱进行设置,只要设置好了,通过邮箱地址和授权码发送邮件

# 1 OOP-Python面向对象
- Python 的面向对象
- 面向对象的编程   
    - 基础
    - 共有私有
    - 继承
    - 组合, Mixin
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
    
# 2 面向对象的概述 (ObjectOriented. OO)
- OOP思想
    - 接触到任意一个任务, 首先想到的是任务这个世界的构成, 是由模型构成的
    - 由命名目标 + 动作  = 任务
- 名词:   
    - OO: 面向对象
    - OOA: 面向对象的分析
    - OOD: 想想对象的设计
    - OOI: XXX的实现
    - OOP: XXXX的编程
    - OOA-> OOD -> OOI: 面向对象实现的过程 
- 类和对象的概念:
    - 类: 抽象名词, 代表一个集合, 共性的事物
    - 对象: 具象的事物,单个个体
    - 类与对象的关系
        - 一个具象,代表一类事物的某一个个体
        - 一个是抽象,代表的是一大类的事物
- 类中的内容, 应该具有两个内容
    - 表明事物的特征,叫做属性(变量)
    - 表明事物或功能的动作,成为成员方法(函数)
# 3 类的基本实现
- 类的命名
    - 遵循变量命名的规范
    - 大驼峰 (由一个或者多个单词构成,每个单词首字母大写,单词跟单词直接相连)
    - 尽量避开跟系统命名相似的命名
- 如何声明一个类
    - 必须用class关键字
    - 类由属性和方法构成,其他不允许出现
    - 成员属性定义可以之间使用变量赋值,如果没有纸,须使用None
        
- 实例化类

        变量 = 类名() # 实例化了一个案例
- 访问对象成员
    - 使用点操作符
    
        obj.成员属性名称
        obj.成员方法

-可以通过默认内置变量价差类的对象的所有成员
   - 对象所有成员检查
   
            # dict前后有两个下划线
            obj.__dict__
   - 类所有的成员
            # dict前后各有两个下划线
            clss_name.__dict__
# 案例 0.1py

# 4 anaconda基本使用
- anaconda 主要是一个虚拟环境
- 还是一个安装包的管理
- conda list : 显示anaconda的安装包
- conda env list : 显示annaconda的虚拟环境的列表
- conda creat -n XXX python=3.6 :创建python版本为3.6的虚拟环境,名为XXX
- conda activate XXX 激活指定虚拟环境
- conda deactivate XXX 取消激活