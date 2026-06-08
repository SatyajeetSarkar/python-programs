class Node:
    def __init__(self, item):
        self.info = item
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Insert at rear
    def enqueue(self, item):
        nd = Node(item)

        if self.front is None:
            self.front = nd
            self.rear = nd
            return

        self.rear.next = nd
        self.rear = nd

    # Delete from front
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return

        item = self.front.info
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return item

    # Display front element
    def peek(self):
        if self.front is None:
            print("Queue Empty")
            return

        print(self.front.info)

    # Display queue
    def display(self):
        if self.front is None:
            print("Queue Empty")
            return

        temp = self.front

        while temp:
            print(temp.info, end=" -> ")
            temp = temp.next

        print("None")


# Driver Code
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()

q.peek()

q.dequeue()

q.display()

q.peek()