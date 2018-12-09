import threading
import time

def loop1(in1):
    print ('Start loop1 at: ', time.ctime())

    print('I am parameter',in1)

    time.sleep(4)

    print('end loop1 at: ',time.ctime())


def loop2(in1,in2):
    print('Start loop2 at: ', time.ctime())

    print('I am parameter', in1, 'and ', in2)

    time.sleep(2)

    print('end loop2 at: ', time.ctime())

def main():
    print('Start main at: ', time.ctime())

    t1 = threading.Thread(target=loop1, args=('lee',))
    t1.start()

    t2 = threading.Thread(target=loop2, args=('Emily','Lily'))
    t2.start()

    t1.join()
    t2.join()


    print('finish at: ', time.ctime())

if __name__ == '__main__':
    main()
