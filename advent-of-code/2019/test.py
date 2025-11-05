import multiprocessing


import testworker

import time

if __name__ == '__main__':
    import time
    import sys

    sys.stdout.write("\rDoing thing %i" % i)
    sys.stdout.flush()
    
    queue = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    outq = multiprocessing.Queue()

    parent_conn, child_conn = multiprocessing.Pipe()
    parent_conn2, child_conn2 = multiprocessing.Pipe()
    
    p = multiprocessing.Process(target=testworker.worker, args=(child_conn,'b'))
    p2 = multiprocessing.Process(target=testworker.worker, args=(child_conn2,'c'))
    p.start()
    p2.start()

    qp = multiprocessing.Process(target=testworker.workerq, args=(queue,'q'))

    qp.start()
    queue.put(555)
    queue.put('END')

    
    
    parent_conn.send(10)    
    parent_conn.send(20)    
    parent_conn.send(30)
    
    parent_conn.send('END')
    parent_conn2.send('a')
    parent_conn2.send('b')
    parent_conn2.send('c')
    parent_conn2.send('END')

    
    
    print('b',parent_conn.recv())
    print('c',parent_conn2.recv())
    
    time.sleep(1)
    print(100000)

    time.sleep(2)
    queue.put('ll')
    
    # Wait for the worker to finish
    queue.close()
    queue.join_thread()
    p.join()

    q2.close()
    q2.join_thread()
    p2.join()

'''
import multiprocessing
import time


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                print('{}: Exiting'.format(proc_name))
                self.task_queue.task_done()
                break
            print('{}: {}'.format(proc_name, next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)


class Task:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1)  # pretend to take time to do the work
        return '{self.a} * {self.b} = {product}'.format(
            self=self, product=self.a * self.b)

    def __str__(self):
        return '{self.a} * {self.b}'.format(self=self)


if __name__ == '__main__':
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # Start consumers
    num_consumers = multiprocessing.cpu_count() * 2
    print('Creating {} consumers'.format(num_consumers))
    consumers = [
        Consumer(tasks, results)
        for i in range(num_consumers)
    ]
    for w in consumers:
        w.start()

    # Enqueue jobs
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    # Add a poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)

    # Wait for all of the tasks to finish
    tasks.join()

    # Start printing results
    while num_jobs:
        result = results.get()
        print('Result:', result)
        num_jobs -= 1




import multiprocessing
import time
import sys


def daemon():
    name = multiprocessing.current_process().name
    print('Starting:', name)
    time.sleep(2)
    print('Exiting :', name)


def non_daemon():
    name = multiprocessing.current_process().name
    print('Starting:', name)
    print('Exiting :', name)


if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
    )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()

'''
