import multiprocessing 
import time 

def worker():
    name = multiprocessing.current_process().name
    print name, 'Starting'
    time.sleep(2)
    print name, 'Exiting'

def my_service():
    name = multiprocessing.current_process().name
    print name, 'Starting'
    time.sleep(2)
    print name, 'Exiting'

if __name__=="__main__":
    service = multiprocessing.Process(name='my_service', target=my_service)
    worker1 = multiprocessing.Process(name='worker1', target=worker)
    worker2 = multiprocessing.Process(target=worker)

    worker1.start()
    worker2.start()
    service.start()

    

