from threading import Semaphore

buffer_size = 10

semaphore_consumer = Semaphore(0)
semaphore_producer = Semaphore(buffer_size)
mutex = Semaphore(1)

# Esta abordagem funciona apenas para o buffer que inicia vazio
# Para a abordagem onde o Buffer inicia cheio é necessario apenas trocar os valores iniciais dos semaforos

def producer():
    semaphore_producer.acquire()
    mutex.acquire()
    print('BUFFER PUT FUNCTION')
    mutex.release()
    semaphore_consumer.release()

def cosumer():
    semaphore_consumer.acquire()
    mutex.acquire()
    print('BUFFER GET FUNCTION')
    mutex.release()
    semaphore_producer.release()

