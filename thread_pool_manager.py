import threading

class ThreadPoolManager(object):
    def __init__(self, max_threads=3) -> None:
        self.max_threads = max_threads
        self.thread_dict: Dict[str, threading.Thread] = {}
        self.thread_result_dict = {}

    def do_task(self, thread_name, num):
        logger.debug(f"执行: {thread_name}")
        self.add_thread_result(thread_name, num**2)

    def remove_thread(self, t_name):
        del self.thread_dict[t_name]

    def add_thread(self, t_name, t):
        self.thread_dict[t_name] = t

    def get_thread_result(self, t_name):
        return self.thread_result_dict[t_name]
    
    def remove_thread_result(self, t_name):
        del self.thread_result_dict[t_name]

    def add_thread_result(self, t_name, result):
        self.thread_result_dict[t_name] = result 

    def threads_count(self):
        return len(self.thread_dict)

    def threads_is_full(self):
        return self.threads_count() >= self.max_threads

    def create_thread(self, t_name, num):
        t = threading.Thread(target=self.do_task, args=(t_name, num))
        self.add_thread(t_name, t)
        t.start()
