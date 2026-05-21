''' Queue Implementation '''

class queue:
    def __init__(self):
        self.queue = [0] * 5
        self.front = -1
        self.rear = -1
        self.MAX = len(self.queue)

    def enque(self, item):
        if self.rear == self.MAX - 1:
            print("Queue overflow")
            return
        if self.front == -1:
            self.front = 0
            self.rear += 1
            self.queue[self.rear] = item 

    def deque(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
            return
        item = self.queue[self.front]
        self.front += 1 
        return item

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        print(self.queue[0])

    def display(self):
        print(self.queue)

q1 = queue()
q1.enque(10)
q1.enque(20)
q1.enque(30)
q1.enque(30)
q1.enque(30)
q1.enque(30)
q1.peek()
