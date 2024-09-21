from threading import *
from time import *

# Class definition for IPC
class MyData():
    def __init__(self):
        self.data = 0 # Data to be consumed by producer and consumer
        self.flag = False # Flag to switch b/w producer and consumer
        self.lock = Lock() 

    def put(self, d):
        # Blocking Mechanism
        while self.flag != False:
            pass

        self.lock.acquire()
        self.data = d
        self.flag = True
        sleep(1)
        self.lock.release()

    def get(self):
        while self.flag != True:
            pass

        self.lock.acquire()
        x = self.data
        self.flag = False
        sleep(1)
        self.lock.release()
        return x

data = MyData()
# Producer producing the data
def producer(data):
    i = 1
    while True:
        data.put(i)
        print("Producer data:", i)
        i += 1
    

def consumer(data):
    while True:
        x = data.get()
        print("Consumer data:", x) 

# Creating the threads
t1 = Thread(target=producer, args=(data,))
t2 = Thread(target=consumer, args=(data,))

# We don't want to call the function immediately, 
# which would block the main thread. Instead, 
# we should pass the function reference and let the thread execute it when the thread starts.


t1.start()
t2.start()

t1.join()
t2.join()