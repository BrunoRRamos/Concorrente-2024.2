from threading import Semaphore

barrier_size = 4

mutex = Semaphore(1)
s1 = Semaphore(0)
s2 = Semaphore(1)
count = 0

# Implementa o metodo wait da barreira REUTILIZAVEL
def wait():
    mutex.acquire()
    global count
    count += 1
    
    if count == barrier_size:
        s1.release()
        s2.acquire()
    mutex.release()
    
    s1.acquire()
    s1.release()

    mutex.acquire()
    global count
    count -= 1

    if count == 0:
        s2.release()
        s1.acquire()
    mutex.release()
