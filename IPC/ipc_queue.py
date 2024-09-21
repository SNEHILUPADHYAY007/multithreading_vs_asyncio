from threading import *
from time import *
from queue import *

# Creating the queue
q = Queue()

# Producer producing the data and pushing in the queue
def producer(q):
    i = 1
    while True:
        q.put(i)
        print("Producer data:", i)
        sleep(1)
        i += 1
    
# Consumer consuming the data from queue
def consumer(q):
    while True:
        x = q.get()
        print("Consumer data:", x) 
        sleep(1)

# Creating the threads
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))

# We don't want to call the function immediately, 
# which would block the main thread. Instead, 
# we should pass the function reference and let the thread execute it when the thread starts.


t1.start()
t2.start()

t1.join()
t2.join()