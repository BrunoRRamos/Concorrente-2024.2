from threading import Thread
from threading import Lock

signalA1 = Lock()
signalA2 = Lock()

signalA1.acquire()
signalA2.acquire()

def a():
    print('action a1')
    signalA1.release()
    signalA2.acquire()
    print('action a2')

def b():
    print('action b1')
    signalA2.release()
    signalA1.acquire()
    print('action b2')

threadA = Thread(target=a)
threadB = Thread(target=b)

threadA.start()
threadB.start()