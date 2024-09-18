from threading import *

def display(str):
    # Locking the fn using MUTEX
    l.acquire()
    
    for i in str:
        print(i)
    # Releasing the fn for other threads
    l.release()

# Creating MUTEX var
l = Lock()

t1 = Thread(target=display, args=("HELLO",))
t2 = Thread(target=display, args=("world",))

t1.start()
t2.start()

t1.join()
t2.join()