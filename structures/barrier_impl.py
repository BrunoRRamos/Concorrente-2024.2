from threading import Semaphore

barrier_size = 4

mutex = Semaphore(1)
s1 = Semaphore(0)
count = 0

# Implementa o metodo wait da barreira NÃO REUTILIZAVEL
def wait():
    mutex.acquire()
    global count
    count += 1
    mutex.release()
    
    if count == barrier_size:
        s1.release()
    
    s1.acquire()
    s1.release()