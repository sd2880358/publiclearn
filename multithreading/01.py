'''
利用time生成两个函数
顺序调用
计算总的运行时间
'''
import time

def loop1():
    print('start loop at: ', time.ctime())
    time.sleep(4)
    print('End loop 1 at :', time.ctime())

def loop2():
    print('start loop at: ', time.ctime())
    time.sleep(2)
    print('End loop 2 at :', time.ctime())

def main():
    print('start loop at: ', time.ctime())
    loop1()
    loop2()
    print('all done: ', time.ctime())

if __name__ == '__main__':
    main()