import threading
import time

flag = True

def increment():
    count = 0
    while flag:
        time.sleep(1)
        count += 1
        print(count)

threading.Thread(target=increment).start()

input("Press y to exit\n")
flag = False