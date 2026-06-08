class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def insert(self, data):
        new_node = Node(data)

        if self.start is None:
            self.start = new_node
            return

        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def reverse(self):
        prev = None
        current = self.start

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.start = prev

    def display(self):
        temp = self.start
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example
ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Original List:")
ll.display()

ll.reverse()

print("Reversed List:")
ll.display()