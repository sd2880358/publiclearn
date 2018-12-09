import threading
import time
# python3 写法
import queue
#python2 from queue import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            #qsize 返回queue 内容长度
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = '生成产品' + str(count)
                    # put 将参数放入queue中
                    queue.put (msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range (3):
                    msg = self.name +'消费了' + queue.get()
                    print(msg)
            time.sleep(0.5)

if __name__ == '__main__':

    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品'+ str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()