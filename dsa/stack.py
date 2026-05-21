''' Stack Implementation '''

class stack:
    def __init__(self):
        self.stack = [0] * 10
        self.top = -1
        self.MAX = len(self.stack)

    def push(self, item):
        if self.stack == self.MAX - 1:
            print("Stack overflow")
            return
        
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.stack == - 1:
            print("Stack underflow")
            return
        
        self.top -= 1

    def peek(self):
        print(self.stack[self.top])

s1 = stack()
s1.push(5)
s1.push(10)
s1.peek()
s1.pop()
s1.peek()