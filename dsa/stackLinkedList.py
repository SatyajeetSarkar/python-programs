class Node:
    def __init__(self, item):
        self.info = item
        self.next = None

class Stack:
    def __init__(self):
        self.start = None

    def push(self, item):
        nd = Node(item)

        if self.start == None:
            self.start = nd
            return
        
        nd.next = self.start
        self.start = nd

    def pop(self):
        if self.start == None:
            print("Underflow")
            return
        
        self.start = self.start.next

    def peek(self):
        if self.start == None:
            print("Underflow")
            return
        
        print(self.start.info)


li = Stack()

li.push(10)
li.push(20)
li.push(30)
li.push(40)

li.peek()

li.pop()
li.pop()
li.pop()
li.pop()

li.peek()