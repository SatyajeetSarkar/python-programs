class Queue:
    def __init__(self):
        self.queue = [0] * 5
        self.front = -1
        self.rear = -1
        self.MAX = len(self.queue)

    def enque(self, item):
        if self.rear == self.MAX - 1:
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = item

    def deque(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return

        item = self.queue[self.front]
        self.front += 1

        if self.front > self.rear:
            self.front = -1
            self.rear = -1

        return item

    def peek(self):
        if self.front == -1:
            print("Queue Empty")
            return

        print(self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue Empty")
            return

        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()


q1 = Queue()

q1.enque(10)
q1.enque(20)
q1.enque(30)
q1.enque(40)
q1.enque(50)

q1.peek()      # 10
q1.display()   # 10 20 30 40 50

q1.deque()

q1.peek()      # 20
q1.display()   # 20 30 40 50