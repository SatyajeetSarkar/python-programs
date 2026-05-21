''' Implementation of Doubly Linked List '''

class Node:
    def __init__(self, item):
        self.info = item
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def insert_at_start(self, item):
        nd = Node(item)

        if self.start is None:
            self.start = nd
            self.end = nd
            return

        nd.next = self.start
        self.start.prev = nd
        self.start = nd

    # Insert at end
    def insert_at_last(self, item):

        nd = Node(item)

        # Empty list
        if self.start is None:
            self.start = nd
            self.end = nd
            return

        self.end.next = nd
        nd.prev = self.end
        self.end = nd

    # Insert at given position
    def insert_at_position(self, item, pos):

        # Position starts from 1
        if pos <= 1:
            self.insert_at_start(item)
            return

        nd = Node(item)

        temp = self.start
        i = 1

        # Move to previous position node
        while temp is not None and i < pos - 1:
            temp = temp.next
            i += 1

        # If position is beyond length
        if temp is None or temp.next is None:
            self.insert_at_last(item)
            return

        nd.next = temp.next
        nd.prev = temp

        temp.next.prev = nd
        temp.next = nd

    # Display forward
    def display(self):

        if self.start is None:
            print("List is Empty")
            return

        temp = self.start

        while temp is not None:
            print(temp.info, end=" <-> ")
            temp = temp.next

        print("None")

    # Display reverse
    def reverse_display(self):

        if self.end is None:
            print("List is Empty")
            return

        temp = self.end

        while temp is not None:
            print(temp.info, end=" <-> ")
            temp = temp.prev

        print("None")


# Driver Code
s1 = LinkedList()

s1.insert_at_start(10)
s1.insert_at_last(20)
s1.insert_at_last(40)

s1.insert_at_position(30, 3)

print("Forward Display:")
s1.display()

print("Reverse Display:")
s1.reverse_display()