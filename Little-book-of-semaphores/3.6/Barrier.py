from threading import Thread
from threading import Lock
from threading import Barrier

mutex = Lock()
barrier = Barrier(4)

count = 0

def sum():
    global count
    with mutex:
        count = count + 1
        print(count)
    barrier.wait()
    print(f'Finalizei {count}')

threads = [Thread(target=sum) for _ in range(4)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()