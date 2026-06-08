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

    # Insertion after specific item
    def insert_after_item(self, item, new_item):
        if self.start is None:
            print("List is Empty")
            return

        temp = self.start

        while temp is not None:
            if temp.info == item:
                nd = Node(new_item)

                nd.prev = temp
                nd.next = temp.next

                if temp.next is not None:
                    temp.next.prev = nd
                else:
                    self.end = nd

                temp.next = nd
                return

            temp = temp.next

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
        self.start.prev = None


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
        self.end.next = None

    # Delete at specific position
    def delete_at_position(self, pos):
        if self.start is None:
            print("Underflow")
            return

        if pos <= 1:
            self.delete_at_start()
            return

        temp = self.start
        i = 1

        while temp is not None and i < pos:
            temp = temp.next
            i += 1

        if temp is None:
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

        while temp is not None:

            if temp.info == item:

                # No node after the item
                if temp.next is None:
                    print("No node exists after", item)
                    return

                del_node = temp.next

                # If deleting the last node
                if del_node == self.end:
                    self.end = temp
                    temp.next = None

                else:
                    temp.next = del_node.next
                    del_node.next.prev = temp

                return

            temp = temp.next

        print("Item not found")

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

s1.insert_at_last(10)
s1.insert_at_last(20)
s1.insert_at_last(30)
s1.insert_at_last(40)

s1.insert_after_item(20, 25)
s1.display()

s1.delete_at_start()
s1.display()

s1.delete_at_last()
s1.display()

s1.delete_at_position(2)
s1.display()

s1.delete_after_item(25)
s1.display()