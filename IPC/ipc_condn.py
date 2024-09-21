from threading import *
from time import *

class MyData:
    def __init__(self):
        self.data = 0
        # Using Condition so that flag and lock steps can be encapsulated
        self.cv = Condition()
    
    # Steps:- Try to Acquire the state, Wait until it is achieved, notify next thread, and release

    def put(self, d):
        self.cv.acquire()
        self.cv.wait(timeout=1)
        self.data = d
        sleep(1)
        self.cv.notify()
        self.cv.release()

    def get(self):
        self.cv.acquire()
        self.cv.wait()
        x = self.data
        sleep(1)
        self.cv.notify()
        self.cv.release()
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