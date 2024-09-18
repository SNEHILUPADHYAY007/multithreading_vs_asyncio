from threading import *

def display(str):
    # Locking the fn using Semaphore
    s.acquire()
    
    for i in str:
        print(i)
    # Releasing the fn for other threads
    s.release()

# Creating Semaphore var
s = Semaphore(2)
# In this case, t1, t2 will execute simultaneously and t3 will w8 until any on the t1,t2 releases the fn. 

t1 = Thread(target=display, args=("HELLO",))
t2 = Thread(target=display, args=("world",))
t3 = Thread(target=display, args=("Snehil",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()