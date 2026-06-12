class Node:
    def __init__(self, item):
        self.info = item
        self.prev = None
        self.next = None


class doublyCircular:
    def __init__(self):
        self.start = None
        self.end = None

    # Insert at start
    def insert_at_start(self, item):
        nd = Node(item)

        if self.start is None:
            self.start = nd
            self.end = nd
            nd.next = nd
            nd.prev = nd
            return

        nd.next = self.start
        nd.prev = self.end

        self.start.prev = nd
        self.end.next = nd

        self.start = nd

    # Insert at end
    def insert_at_last(self, item):
        nd = Node(item)

        if self.start is None:
            self.start = nd
            self.end = nd
            nd.next = nd
            nd.prev = nd
            return

        nd.prev = self.end
        nd.next = self.start

        self.end.next = nd
        self.start.prev = nd

        self.end = nd

    # Insert at position
    def insert_at_position(self, item, pos):

        if pos <= 1 or self.start is None:
            self.insert_at_start(item)
            return

        temp = self.start
        i = 1

        while i < pos - 1 and temp.next != self.start:
            temp = temp.next
            i += 1

        if temp == self.end:
            self.insert_at_last(item)
            return

        nd = Node(item)

        nd.next = temp.next
        nd.prev = temp

        temp.next.prev = nd
        temp.next = nd

    # Insert after specific item
    def insert_after_item(self, item, new_item):

        if self.start is None:
            print("List is Empty")
            return

        temp = self.start

        while True:

            if temp.info == item:
                nd = Node(new_item)

                nd.prev = temp
                nd.next = temp.next

                temp.next.prev = nd
                temp.next = nd

                if temp == self.end:
                    self.end = nd

                return

            temp = temp.next

            if temp == self.start:
                break

        print("Item not found")

    # Delete at start
    def delete_at_start(self):

        if self.start is None:
            print("Underflow")
            return

        if self.start == self.end:
            self.start = None
            self.end = None
            return

        self.start = self.start.next

        self.start.prev = self.end
        self.end.next = self.start

    # Delete at end
    def delete_at_last(self):

        if self.start is None:
            print("Underflow")
            return

        if self.start == self.end:
            self.start = None
            self.end = None
            return

        self.end = self.end.prev

        self.end.next = self.start
        self.start.prev = self.end

    # Delete at position
    def delete_at_position(self, pos):

        if self.start is None:
            print("Underflow")
            return

        if pos <= 1:
            self.delete_at_start()
            return

        temp = self.start
        i = 1

        while i < pos and temp.next != self.start:
            temp = temp.next
            i += 1

        if i < pos:
            print("Invalid Position")
            return

        if temp == self.end:
            self.delete_at_last()
            return

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    # Delete after specific item
    def delete_after_item(self, item):

        if self.start is None:
            print("Underflow")
            return

        temp = self.start

        while True:

            if temp.info == item:

                if temp.next == self.start:
                    print("No node exists after", item)
                    return

                del_node = temp.next

                if del_node == self.end:
                    self.delete_at_last()
                else:
                    temp.next = del_node.next
                    del_node.next.prev = temp

                return

            temp = temp.next

            if temp == self.start:
                break

        print("Item not found")

    # Display forward
    def display(self):

        if self.start is None:
            print("List is Empty")
            return

        temp = self.start

        while True:
            print(temp.info, end=" <-> ")
            temp = temp.next

            if temp == self.start:
                break

        print("(START)")

    # Display reverse
    def reverse_display(self):

        if self.end is None:
            print("List is Empty")
            return

        temp = self.end

        while True:
            print(temp.info, end=" <-> ")
            temp = temp.prev

            if temp == self.end:
                break

        print("(END)")


# Driver Code

dll = doublyCircular()

dll.insert_at_last(10)
dll.insert_at_last(20)
dll.insert_at_last(30)
dll.insert_at_last(40)

print("Original List:")
dll.display()

dll.insert_after_item(20, 25)
print("\nAfter inserting 25 after 20:")
dll.display()

dll.delete_at_start()
print("\nAfter deleting start:")
dll.display()

dll.delete_at_last()
print("\nAfter deleting end:")
dll.display()

dll.delete_at_position(2)
print("\nAfter deleting position 2:")
dll.display()

dll.delete_after_item(25)
print("\nAfter deleting node after 25:")
dll.display()

print("\nReverse Display:")
dll.reverse_display()