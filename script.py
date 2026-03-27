from queue_model import Queue
from process_model import Process

queue = Queue()

def create_processes(quantity: int, queue: Queue):
    for i in range(quantity):
        time = (i + 1) * 2
        queue.enqueue(Process(i, time))
    return queue

create_processes(3, queue)

print(queue)