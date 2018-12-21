import _thread as thread
import time

def loop1():
    print('start loop1 at: ', time.ctime())
    time.sleep(4)
    # print('End loop 1 at : ', time.ctime())

def loop2():
    print('start loop2 at: ', time.ctime())
    time.sleep(2)
    print('End loop 2 at :', time.ctime())

def main():
    print('start loop at: ', time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程的函数为 start_new_thead
    # 参数两个,一个需要运行函数名,第二个参数作为元组使用,为空则使用空元祖
    # 注意:如果函数只有一个参数,需要参数后有一个逗号
    thread.start_new_thread(loop1,())

    thread.start_new_thread(loop2,())


    print('all done: ', time.ctime())

if __name__ == '__main__':
    main()
