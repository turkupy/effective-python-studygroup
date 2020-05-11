import threading
import time

# Program will hang when using Lock(), but will run w/o error with RLock()
# RLock is a re-entrant lock

lock = threading.Lock()
#lock = threading.RLock()

num = 5

def add():
    global num
    with lock:
        num += 10
    print(num)

def multiply():
    global num
    with lock:
        num *= 2
    print(num)

def calculate_something():
    global num
    # here we try to acquire the same lock twice
    # RLock() allows us to do so, but Lock() blocks
    with lock:
        add()
        multiply()
    print(num)

calculate_something()