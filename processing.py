"""
pipe、queue、event、condition、signal(linux)、semaphore、value、share_memory 多进程通信
"""
import os
import time
from multiprocessing import Process, Pipe, Queue, Event, Condition
from multiprocessing.connection import PipeConnection
from multiprocessing.synchronize import Event as EV
# from multiprocessing.queues import Queue
from loguru import logger
import random



# def child_process1(conn: PipeConnection):
#     logger.debug("child_process1 pid: %s, ppid: %s  do task" % (os.getpid(), os.getppid()))
#     time.sleep(3)
#     msg = conn.recv()
#     logger.info("receive msg: %s" % msg)
#     conn.send("msg: %s hello" % msg)
#     conn.close()
#     logger.debug("child_process1 end")

# def child_process2(conn: PipeConnection):
#     try:
#         logger.debug("child_process2 pid: %s, ppid: %s  do task" % (os.getpid(), os.getppid()))
#         time.sleep(6)
#         logger.debug("child_process2 end")
#     except Exception as e:
#         conn.send("fail")
#     else:
#         conn.send("success")
#     finally:
#         msg = conn.recv()
#         logger.warning("receive msg: %s" % msg)
#         conn.close()

# def main():
#     conn1, conn2 = Pipe(duplex=True)
#     process1 = Process(target=child_process1, args=(conn1,))
#     process2 = Process(target=child_process2, args=(conn2,))
#     process1.start()
#     process2.start()
#     print("main pid: %s" % os.getpid())
#     time.sleep(4)
#     print("main end")

# def child_process1(q: Queue):
#     while True:
#         data = q.get()
#         time.sleep(random.choice([1,2,3]))
#         logger.warning("child_process1 get -> %s" % data)

# def child_process2(q: Queue):
#     while True:
#         data = q.get()
#         time.sleep(random.choice([1,2,3]))
#         logger.error("child_process2 get -> %s" % data)
        

# def main():
#     """
#     队列通信
#     """
#     queue = Queue(maxsize=10)
#     p1 = Process(target=child_process1, args=(queue,))
#     p2 = Process(target=child_process2, args=(queue,))
#     p1.start()
#     p2.start()
#     for i in range(10):
#         queue.put(i)
#     logger.info("main end")


# def child_process1(ev: EV):
#     """
#     和process3一样同步执行
#     """
#     logger.debug("start child process1")
#     if not ev.is_set():
#         ev.wait()
#     logger.debug("ev is set")
#     time.sleep(3)
#     logger.debug("end child process1")

# def child_process2(ev: EV):
#     """
#     先执行
#     """
#     logger.warning("start child process2")
#     ev.clear()
#     time.sleep(2)
#     logger.warning("process2 task finish")
#     ev.set()
#     logger.warning("process2 end")

# def child_process3(ev: EV):
#     """
#     和process1一样同步执行
#     """
#     logger.info("start child process3")
#     if not ev.is_set():
#         ev.wait()
#     logger.info("ev is set")
#     time.sleep(6)
#     logger.info("end child process3")


# def main():
#     """
#     event 通信
#     """
#     event = Event()
#     p1 = Process(target=child_process1, args=(event,))
#     p2 = Process(target=child_process2, args=(event,))
#     p3 = Process(target=child_process3, args=(event,))
#     p1.start()
#     p2.start()
#     p3.start()
#     p1.join()
#     p2.join()
#     p3.join()


# import os
# import signal
# import time
# from multiprocessing import Process


# def child():
#     def receive_signal(signum, frame):
#         print("Child {} received signal: {}".format(os.getpid(), signum))

#     # 注册信号处理程序
#     signal.signal(signal.SIGINFO, receive_signal)

#     print("Child {} waiting for signal...".format(os.getpid()))
#     while True:
#         time.sleep(1)


# def parent(children):
#     # 发送信号给子进程
#     for child_proc in children:
#         print("Sending signal to child {}...".format(child_proc.pid))
#         os.kill(child_proc.pid, signal.SIGINFO)

#     # 等待一段时间
#     time.sleep(2)

#     # 发送停止信号给子进程
#     for child_proc in children:
#         print("Sending stop signal to child {}...".format(child_proc.pid))
#         os.kill(child_proc.pid, signal.SIGTERM)

#     # 等待子进程退出
#     for child_proc in children:
#         child_proc.join()


# if __name__ == "__main__":
#     children = []
#     for _ in range(3):
#         child_proc = Process(target=child)
#         child_proc.start()
#         children.append(child_proc)

#     parent(children)



# import multiprocessing
# import time

# def process_a(semaphore):
#     print("Process A is waiting...")
#     semaphore.acquire()
#     print("Process A has acquired the semaphore.")
#     time.sleep(2)
#     print("Process A is releasing the semaphore.")
#     semaphore.release()

# def process_b(semaphore):
#     time.sleep(1)
#     print("Process B is waiting to acquire the semaphore...")
#     semaphore.acquire()
#     print("Process B has acquired the semaphore.")
#     print("Process B is releasing the semaphore.")
#     semaphore.release()

# if __name__ == "__main__":
#     semaphore = multiprocessing.Semaphore(1)  # 初始化信号量，初始值为1

#     # 创建两个进程
#     process1 = multiprocessing.Process(target=process_a, args=(semaphore,))
#     process2 = multiprocessing.Process(target=process_b, args=(semaphore,))

#     # 启动进程
#     process1.start()
#     process2.start()

#     # 等待进程结束
#     process1.join()
#     process2.join()

#     print("All processes have finished.")




# import multiprocessing
# import time

# def producer(condition, shared_list):
#     for i in range(1, 6):
#         with condition:
#             print(f"Producer: Producing item {i}")
#             shared_list.append(i)
#             condition.notify()  # 通知消费者
#         time.sleep(1)

# def consumer(condition, shared_list):
#     while True:
#         with condition:
#             while not shared_list:
#                 print("Consumer: Waiting for items to be produced...")
#                 condition.wait()  # 等待生产者通知
#             item = shared_list.pop(0)
#             print(f"Consumer: Consuming item {item}")
#         time.sleep(2)

# if __name__ == "__main__":
#     condition = multiprocessing.Condition()
#     shared_list = multiprocessing.Manager().list()  # 创建共享列表

#     producer_process = multiprocessing.Process(target=producer, args=(condition, shared_list))
#     consumer_process = multiprocessing.Process(target=consumer, args=(condition, shared_list))

#     producer_process.start()
#     consumer_process.start()

#     producer_process.join()
#     consumer_process.terminate()




# import multiprocessing

# def process_task(shared_var):
#     shared_var.value += 1
#     print(f"Process {multiprocessing.current_process().pid}: Incremented shared variable to {shared_var.value}")

# if __name__ == "__main__":
#     shared_var = multiprocessing.Value('i', 0)  # 创建一个共享整型变量

#     processes = []
#     for _ in range(5):
#         process = multiprocessing.Process(target=process_task, args=(shared_var,))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()

#     print(f"Final shared variable value: {shared_var.value}")



# import multiprocessing
# from multiprocessing import shared_memory

# def writer(shared_memory):
#     with shared_memory as memory:
#         for i in range(5):
#             memory[0] = i
#             print("Writer wrote:", i)

# def reader(shared_memory):
#     with shared_memory as memory:
#         for _ in range(5):
#             print("Reader read:", memory[0])

# if __name__ == "__main__":
#     # 创建共享内存
#     with multiprocessing.shared_memory.SharedMemory(create=True, size=4) as shared_memory:
#         # 创建写入进程和读取进程
#         writer_process = multiprocessing.Process(target=writer, args=(shared_memory,))
#         reader_process = multiprocessing.Process(target=reader, args=(shared_memory,))

#         # 启动进程
#         writer_process.start()
#         reader_process.start()

#         # 等待进程结束
#         writer_process.join()
#         reader_process.join()






