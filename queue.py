class Node:
    def __init__(self, data=None):
        self.data = data            
        self.next = None            

class Queue:
    def __init__(self):
        self.head = None            
        self.tail = None            
        self._size = 0              
    
    def enqueue(self, elem):
        node = Node(elem)
        if self.tail is None:           
            self.tail = node            
            self.head = node            
        else:
            self.tail.next = node       
            self.tail = node            
        self._size = self._size + 1
    
    def dequeue(self):
        if self._size > 0:
            elem  = self.head.data
            self.head = self.head.next
            self._size = self._size - 1
            return elem
        raise IndexError("The queue is empty")

    def front(self):
        if self._size > 0:
            elem = self.head.data
            return elem
        raise IndexError("The queue is empty")

    def __len__(self):
        return self._size
    
    def show(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next