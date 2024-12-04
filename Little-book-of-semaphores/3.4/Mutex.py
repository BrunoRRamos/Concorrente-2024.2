from threading import Thread
from threading import Lock

mutex = Lock()

count = 0

def sum():
    global count
    with mutex:
        count = count + 1

threads = []

for _ in range(1000):
    threadA = Thread(target=sum)
    threadB = Thread(target=sum)
    threads.append(threadA)
    threads.append(threadB)
    threadA.start()
    threadB.start()


for thread in threads:
    thread.join()

print(count)