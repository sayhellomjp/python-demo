import random, time, queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#接收任务的队列
result_queue = queue.Queue()

def return_task_queue():
    return task_queue

def return_result_queue():
    return result_queue

class QueueManager(BaseManager):
    pass

def process_start():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'777')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('put task %d...' % n)
        task.put(n)

    print('开始取数据')

    for i in range(10):
        try:
            r = result.get(timeout=5)
            print('result: %s' % r)
        except:
            print('result queue is empty')


    manager.shutdown()
    print('master exit')

if __name__ == '__main__':
    print('start')
    process_start()





