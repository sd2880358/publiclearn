from multiprocessing import Process

import os

def info(title):
    print(title)
    print('module name',__name__)
    # 得到父进程id
    print('parents process', os.getppid())
    # 得到本身进程的id
    print('process id ', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()