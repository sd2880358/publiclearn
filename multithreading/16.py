import threading
import time

num = 0

class Mythread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
            # 可重入锁
        if mutex.acquire(1):
            num += 1
            msg = self.name + 'set num to ' + str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

mutex = threading.RLock()

def thtest():
    for i in range(5):
        t = Mythread()
        t.start()

if __name__ == '__main__':
    thtest()