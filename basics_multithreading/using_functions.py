from threading import *

# To display ASCII characters using Alphabet thread
def display():
    for i in range(65,91):
        print(chr(i))

# Creating object of Thread 
thread = Thread(target = display, name = 'Alphabet')
# Starting thread object to start executing
thread.start()


# Main Thread code
for i in range(65,91):
    print(i)

print("Completed executing main thread")

# Will make sure that main stops after thread completion
thread.join()