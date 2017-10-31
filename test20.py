from multiprocessing import Process, Queue
import os, time, random, threading


# def run_proc(name):
#     print("子进程启动:%s (%s)" % (name, os.getpid()))
#
# if __name__ == '__main__':
#     print("主进程启动 %s" % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print("子进程即将启动")
#     p.start()
#     p.join()
#     print("子进程启动完毕")


# def write(q):
#     print("写入进程 %s" % os.getpid())
#     for v in ['A', 'B', 'C']:
#         print("放入队列,值:%s" % v)
#         q.put(v)
#         time.sleep(random.random())
#
# def read(q):
#     print("读取进程 %s" % os.getpid())
#     while True:
#         v = q.get(True)
#         print('从队列取值 %s' % v)
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()

# def loop():
#     print('thread %s is running' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n =  n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended' % threading.current_thread().name)
#
# print('thread %s is running' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)

# balance = 0
# lock = threading.Lock()
#
# def change_value(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_loop(n):
#     for x in range(10000000):
#         lock.acquire()
#         try:
#             change_value(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run_loop, args=(5,))
# t2 = threading.Thread(target=run_loop, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('result:', balance)

# class Student():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# global_dict = {}
#
#
# def std_thread(std):
#     global_dict[threading.current_thread()] = std
#     do_task1()
#     do_task2()
#
# def do_task1():
#     print("thread %s task1: %s" % (threading.current_thread().name, global_dict[threading.current_thread()].name))
#
# def do_task2():
#     print("thread %s task2: %s" % (threading.current_thread().name, global_dict[threading.current_thread()].name))
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=std_thread, args=(Student("majunpeng", 26),), name='Thread1')
#     t2 = threading.Thread(target=std_thread, args=(Student("rtt", 26),), name='Thread2')
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("done")


local_student = threading.local()


def run_process():
    student_name = local_student.student_name
    print('Hello, %s in %s' % (student_name, threading.current_thread().name))

def process_thread(student_name):
    local_student.student_name = student_name
    run_process()

t1 = threading.Thread(target=process_thread, args=('mjp',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('rtt',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()




