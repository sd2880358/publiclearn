# 环境

# 多线程 vs 多进程

- 程序: 一堆代码以文本形式存入一个文档
- 进程: 程序运行的一个状态
    - 包含地址控件,内存,数据栈
    - 每个进程由自己完全独立运行环境,多进程共享数据是一个问题
- 线程: 
    - 一个进程的独立运行片段,一个进程可以有多个线程
    - 轻量化的进程
    - 一个京城的那个的多个线程间空想数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁(GIL:GlobalInterpretationLocker)
    - python代码的执行是由python虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行

- python包
    - thread:有问题,不好用,python3改成了_thread
    - threading(2.0):通行的包

- 案例01:顺序执行,耗时较长
- 案例p02:改用多线程,缩短耗时,使用_thread
- 案例03: 多线程,传参数

- threading 的使用
    - 直接利用 threading.Thread 生成Thread实例
        1. t = threading.Thread(target=xxx,args=(xxx,))
        2. t.start(): 启动多线程
        3. t.join(): 等待多线程执行完成
        4. 案例04: 加入join后线程按条执行
    - 守护线程: setDaemon(True)
        - 如果在程序中将子线程设置成守护线程,则子线程会在主线程结束的时候自动退出
        - 一般认为,守护线程不重要或者不允许离开主线程独立运行
        - 守护线程案例是否有效果跟环境相关
        - 案例05
    - 线程常用属性
        - threading.currentThread: 返回当前线程变量
        - threading.enumerate: 返回一个包含正在运行的线程的list,正在运行的线程指的是线程启动后,结束前
        - threading.activeCount: 返回正在运行的线程的数量,效果跟len(threading.enmerate)仙童
        - thr.setName: 给线程设置名字
        - thr.getName: 得到线程的名字
        案例06
    - 直接继承threading.Thread
        - 直接继承Thread
        - 重写run函数
        - 类实例可以直接运行
        - 案例07
        - 案例08 工业风案例
- 共享变量
    - 共享变量: 当多个线程同时访问一个变量的时候,会产生共享变量的问题
    - 案例09    
    - 解决变量: lock,signal
    - 案例10
    - lock: 
        - 是一个标志,表示一个线程在占用一些资源
        - 使用方法:
            - 上锁
            - 使用共享资源,放心的用
            - 取消锁, 释放锁
        - 锁谁,哪个资源需要多个线程共享,锁哪个
        - 理解锁:锁其实不是锁住谁,而是一个令牌
    - 线程安全问题:
        - 如果一个资源/变量,ta对于多线程来说,不会加锁也不会引起任何问题,则成为线程安全
        - 线程不安全变量,list,set,dict
        - 线程安全变量类型,queue
    - 生产者消费者问题:
        - 一个模型,可以用来搭建消息队列,案例11
        - queue是一个用来存放变量的数据结构,特点是先进先出,内部元素派对,可以理解成一个特殊的list
    - 死锁问题: 案例12
    - 锁的等待时间问题 案例13
    - semphore 
        - 允许一个资源最多有几个线程同时使用
        - 案例14
    - threading.Timer :启动倒计时(sec,func)
        - 案例15
     
    - 可重入锁 RLock
        - 一个锁,可以被一个线程多次申请
        - 主要解决递归调用的时候, 需要申请锁的情况
        - 案例16
        
# 线程代替方案
- subprocess
    - 完全跳过线程,使用进程
    - 是派生进程的主要替代方案
    - python2.4后引入
- multiprocessiong
    - 使用threading 接口,使用子进程
    - 允许为多核或者多cpu派生进程,与threading非常相似
    - python2.6
- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    - python3.2引入
# 多进程
- 进程间通讯(InterprocessCommunication,IPC)
- 进程之间无任何共享状态
- 进程的创建
    - 直接生成Process实例对象,案例17
    - 派生子类,案例18
- 在os 中可以查看pid, ppid以及他们的关系
    - 案例19
- 生产者消费者模型
    - 案例20
    - JoinableQueue
    - 队列中哨兵的使用,案例21
    - 哨兵的改进, 案例22