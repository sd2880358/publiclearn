import _thread as thread
import time

def loop1(in1):
    print ('Start loop1 at: ', time.ctime())

    print('I am paramater',in1)

    time.sleep(4)

    print('end loop1 at: ',time.ctime())


def loop2(in1,in2):
    print('Start loop2 at: ', time.ctime())

    print('I am paramater', in1, 'and ', in2)

    time.sleep(2)

    print('end loop2 at: ', time.ctime())

def main():
    print('Start main at: ', time.ctime())

    thread.start_new_thread(loop1, ('lee',))

    thread.start_new_thread(loop2, ('Emily', 'Lily'))

    print('finish at: ', time.ctime)

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)