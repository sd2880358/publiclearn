# 1. 模块
- 一个模块就是包含python代码的文件,后缀名是(.py)就可以,
模块就是python的文件
- 模块的原因:
    - 程序太大,编写维护非常不方便,需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用,避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件,所以任何代码可以直接书写
    - 不过根据模块的范围,最好在模块编写以下内容:
        - 函数(单一功能)
        - 类 (相似功能的组合,或者类似业务模块)
        - 测试代码

- 如何使用模块
    - 模块直接导入
        - 加入模块名字以数字开头不能运行 
        - 假如模块以数字开头,需要导入函数 importlib 函数如下
            ` import importlib
              XXX = importlib.import_module('数字名称')'
              XJMC = XXXX.XXXX()`
       
    - 语法
    
           import model_name
           moudle_name.function_name
           moudle_name.class_name
    - import 模块 as 别名
        - 导入的同事给模块起一个别名
        - 其余用法跟第一个相同
        - 案例03
   
    - from module_name import func_name/class_name
        - 按上述方法有选择性的导入函数
        - 使用的时候可以直接使用导入的函数,不需要前缀
        - 案例04
    - from module_name import *
        - 导入模块所有内容
        - 案例05
    - if __name__ == '__main__':
        - 如果文件作为主文件使用,使用命令
        - 如果作为调用则不使用
        - 建议所有程序都以此程序作为入口
        - 案例 p01
        
# 2. 模块的搜索路径和存储
- 什么是模块的搜索路径:
    - 加载模块的时候,系统会在哪些地方寻找此模块
- 系统默认的搜索路径


        import sys
    sys.path 属性可以获取路径的列表
    
- 添加搜索路径
    
            
            'sys.path.apend[]'
            
- 模块的加载顺序
    - 1. 搜索内存中已经加载好的模块
    - 2. 搜索python的内置模块
    - 3. 搜索sys.path路径
    
# 3. 包 
- 包是一种组织管理代码的方式,包里面存放的是模块
    - 用于将模块包含在一起的文件夹就是包
- 自定义的包的结构


            /--- 包
            /---/--- __init__.py 包的标志文件
            /---/--- 模块1
            /---/--- 模块2
            /---/--- 子包(文件夹)
            /---/---/--- __init__.py 子包文件夹中标志文件
            /---/---/--- 子包模块1
            /---/---/--- 子包模块2
            
-  包的导入操作
    - import package_name
        - 直接导入一个包,可以使用__init__.py的内容
        - 使用的方式:
                
                package_name.func_name
                package_name.class_name.func_name()
        - 案例 pkg01,p07.py
    - import package_name as p
        - 具体用法跟作用方式和上述简单导入一致
        - 注意的事此种用法对默认init.py内容的导入
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
        
                package.module.func_name()
                package.module.class.fun()
                package.module.class.var()
        - 案例p08
    - import package.name.module as p
    
- from ...import 导入
    - from package import module1,module2....
    - 此种导入方法不执行'__init__'的内容
    
            form pkg01 import p01
            p01.sayHello()
    - from package import *
        - 导入当前包'__init__'文件中的所有内容
        - 使用方法
        
                func_name()
                class_name.func_name()
                class_name.var
        - 案例p09
    - from package.module import *
        - 导入这个包的所有内容
                    
                    fuc_name()
                    class_name.func_name()
                    
- 在开发环境中经常会使用其他的模块,可以在当前包中直接导入其他模块中的内容
    - import 完整的包或者模块的路径

- `__all__` 的用法
    - 在使用from package import * 的时候,(* 可以导入的内容)
    - `__init__.py`中如果文件夹为空,或者没有`__all__`,只可以吧`__init__`的内容
    - `__init__`如果设置了`__all__`的值,那么按照`__all__`的指定子包或者模块进行导入
        - 如此则不会载入`__init__`的内容
            `__all__` = [module1,module2]

# 3. 命名空间
- 用于区分于不同位置不同功能但相同名称的函数或者变量的一个特定前缀
- 作用是防止命名冲突

     setName()
     Student.setName()
     Dog.setName()