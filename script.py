from queue_model import Queue
from process_model import Process

queue = Queue()

def create_processes(quantity: int, queue: Queue):
    for i in range(quantity):
        time = (i + 1) * 2
        queue.enqueue(Process(i, time))
    return queue

create_processes(3, queue)

def proccess_queues(queue: Queue, quantum: int):
    process = queue.head
    while process:
        if not isinstance(process.data, Process):
            process = process.next
        if (process.data.remaining_time <= 0):
            queue.dequeue()
            process = process.next

        finished = False

        for _ in range(quantum):
            process.data.remaining_time -=1
            
            if (process.data.remaining_time == 0):
                queue.dequeue()
                finished = True
                break

        if finished:
            process = process.next
            continue
        
        pending_process = process.data
        queue.dequeue()
        queue.enqueue(pending_process)

proccess_queues(queue, 4)