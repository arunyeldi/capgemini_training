import threading
import time

print("Main thread started")

def task_1():
    print("The task 1 started")
    time.sleep(2)
    print("The task 1 completed")

def task_2():
    print("The task 2 started")
    time.sleep(2)
    print("The task 2 completed")

thread_1 = threading.Thread(target=task_1)
thread_2 = threading.Thread(target=task_2)
thread_1.start()
thread_2.start()
thread_2.join()
print("Main thread execution completed")