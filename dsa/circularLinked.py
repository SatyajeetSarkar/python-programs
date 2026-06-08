''' Implementation of Circular Linked List '''

class node:
    def __init__(self, item):
        self.info = item
        self.next = None
    
class linked_list:
    def __init__(self):
        self.start = None

    # Insert at start
    def insert_at_start(self, item):
        nd = node(item)

        if self.start is None:
            self.start = nd
            nd.next = self.start
            return
        
        temp = self.start
        while temp.next != self.start:
            temp = temp.next
        
        nd.next = self.start
        temp.next = nd
        self.start = nd

    # Delete at start
    def delete_at_start(self):
        if self.start is None:
            print("No item found")
            return
        
        temp = self.start
        while temp.next != self.start:
            temp = temp.next

        temp.next = self.start.next
        self.start = self.start.next

    # Delete at the end
    def delete_at_end(self):
        if self.start is None:
            print("No item found")
            return

        if self.start.next == self.start:
            self.start = None
            return

        prev = None
        temp = self.start

        while temp.next != self.start:
            prev = temp
            temp = temp.next

        prev.next = self.start

    # Delete at specific position
    def delete_at_position(self, pos):
        if self.start is None:
            print("No item found")
            return

        if pos == 1:
            self.delete_at_start()
            return

        prev = None
        temp = self.start
        count = 1

        while count < pos and temp.next != self.start:
            prev = temp
            temp = temp.next
            count += 1

        if count != pos:
            print("Invalid Position")
            return

        prev.next = temp.next

    # Insert after specific item
    def delete_after_item(self, item):
        if self.start is None:
            print("No item found")
            return

        temp = self.start

        while True:
            if temp.info == item:
                if temp.next == self.start and temp == self.start:
                    print("No node after item")
                    return

                delete_node = temp.next

                if delete_node == self.start:
                    self.delete_at_start()
                else:
                    temp.next = delete_node.next

                return

            temp = temp.next

            if temp == self.start:
                break

        print("Item not found")

    # Insert at last
    def insert_at_last(self, item):
        nd = node(item)

        if self.start is None:
            self.start = nd
            nd.next = self.start
            return
        
        temp = self.start
        while temp.next != self.start:
            temp = temp.next
        
        temp.next = nd
        nd.next = self.start

    # Insert at specific position
    def insert_at_position(self, item, pos):
        if pos == 1:
            self.insert_at_start(item)
        else:
            nd = node(item)
            i = 1
            temp = self.start
            while i<pos-1 and temp.next != self.start :
                temp = temp.next
                i += 1

            if temp.next == self.start:
                return
            nd.next = temp.next
            temp.next = nd

    # Insert after a specific item
    def insert_after_item(self, item, s_item):
        nd = node(item)
        temp = self.start
        while temp.next != self.start and temp.info != s_item:
            temp = temp.next

        if temp.next == self.start:
            return
        
        nd.next = temp.next
        temp.next = nd
    
    def display(self):
        if self.start is None:
            print("List is empty")
        else:
            temp = self.start
            while temp.next != self.start:
                print(f"{temp.info} ->", end=" ")
                temp = temp.next
            print(temp.info)

            


s1 = linked_list()

print("Insertions:")
s1.insert_at_start(10)
s1.insert_at_start(15)
s1.insert_at_position(20, 1)
s1.insert_after_item(30, 20)
s1.display()

print("Deletions:")
s1.delete_at_start()
# s1.insert_at_last(10)
s1.display()