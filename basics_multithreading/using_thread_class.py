from threading import *

# Creating Alphabet class inheriting Thread class
class Alphabet(Thread):
    # Overwriting run method of Thread class to our usecase
    def run(self):
        for i in range(65,91):
            print(chr(i))

# Creating Alphabet Object
thread = Alphabet()
# Starting the thread
thread.start()

for i in range(65,91):
    print(i)

print("Main executed successfully")
thread.join()