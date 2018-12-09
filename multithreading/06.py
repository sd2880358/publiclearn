import threading
import time

def loop1(in1):
    print ('Start loop1 at: ', time.ctime())

   # print('I am parameter',in1)

    time.sleep(4)

    print('end loop1 at: ',time.ctime())


def loop2():
    print('Start loop2 at: ', time.ctime())

   # print('I am parameter', in1, 'and ', in2)

    time.sleep(2)

    print('end loop2 at: ', time.ctime())

def loop3():
    print('loop3 start at: ', time.ctime())
    time.sleep(5)
    print('loop3 finished at: ', time.ctime())

def main():
    print('Start main at: ', time.ctime())

    t1 = threading.Thread(target=loop1, args=('lee',))
    t1.setName('THR_1')
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName('THR_2')
    t2.start()
    t3 = threading.Thread(target=loop3, args=())
    t3.setName('THR_3')
    t3.start()

    #t1.join()
    #t2.join()
    #t3.join()

    for thr in threading.enumerate():
        print('正在运行的线程名字是{0}'.format(thr.getName()))

    print('正在运行线程的数量为{0}'.format(threading.active_count()))

    print('finish at: ', time.ctime())

if __name__ == '__main__':
    main()
