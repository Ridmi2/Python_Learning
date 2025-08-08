import time
from threading import *
import threading

lock = Lock()
def display():
    lock.acquire()
    for i in range(5):
       
       print(threading.currentThread().name)
       time.sleep(1)
    lock.release()
t1=Thread(target=display)
t2=Thread(target=display)
t1.start()
t2.start() 