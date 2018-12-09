import threading
import time

class myThread(threading.Thread):
    def __init__(self,arg):
        super(myThread,self).__init__()
        self.arg = arg

    def run(self):
        time.sleep(2)
        print('the args for this class is {0}'.format(self.arg))

for i in range(5):
    t = myThread(i)
    t.start()
    t.join()

print('main thread is done!')