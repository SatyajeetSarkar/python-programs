''' Implementation of Circular Queue'''

class circular_queue:
    def __init__(self):
        self.queue = [0] * 10
        self.front = -1
        self.rear = -1
        self.MAX = len(self.queue)

    # Queue Enque 
    def enque(self, item):
        if (self.rear + 1) % self.MAX == self.front:
            print("Queue overflow")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.MAX
            
        self.queue[self.rear] = item 

    # Queue Deque
    def deque(self):
        if self.front == -1:
            print("Queue underflow")
            return

        temp = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.MAX

        return temp
    
    # Queue Peek
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        print(self.queue[0])

    def display(self):
        print(self.queue)

q1 = circular_queue()
q1.enque(10)
q1.enque(20)
q1.enque(30)
q1.peek()

q1.deque()
q1.peek()