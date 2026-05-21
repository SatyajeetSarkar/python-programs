''' Linked List Implementation '''

class node:
    def __init__(self, item):
        self.info = item
        self.next = None
    
class linked_list:
    def __init__(self):
        self.start = None

    def insert_at_last(self, item):
        nd = node(item)
        if self.start == None:
            self.start = nd
            return
        
        temp = self.start
        while temp.next != None:
            temp = temp.next
        temp.next = nd

    def insert_at_start(self, item):
        nd = node(item)
        nd.next = self.start
        self.start = nd

    def insert_at_position(self, item, pos):
        if pos == 1:
            self.insert_at_start(item)
        else:
            nd = node(item)
            i = 1
            temp = self.start
            prev = None
            while temp != None and i<pos:
                prev = temp
                temp = temp.next
                i += 1
            if prev  == None:
                temp.next = nd
                return
            nd.next = temp
            prev.next = nd           

    def insert_after_specific_item(self, item, specific_item):
        nd = node(item)
        temp = self.start
        while temp.next != None and temp.info != specific_item:
            temp = temp.next
        nd.next = temp.next
        temp.next = nd

    def delete_start(self):
        temp = self.start
        self.start = temp.next
        del temp

    def delete_at_last(self):
        temp = self.start
        while temp.next != None:
            prev = temp
            temp = temp.next
        prev.next = None
        del temp

    def delete_at_position(self, pos):
            i = 1
            temp = self.start
            prev = None
            while temp.next != None and i<pos:
                prev = temp
                temp = temp.next
                i += 1
            if temp.next == None:
                return
            prev.next = temp.next
            del temp     

    def delete_after_specific_item(self, specific_item):
        temp = self.start
        while temp.next != None and temp.info != specific_item:
            temp = temp.next
        temp_nd = temp.next
        temp.next = temp_nd.next
        del temp_nd

    def display(self):
        if self.start is None:
            print("List is empty")
        else:
            temp = self.start
            while temp.next != None:
                print(f"{temp.info} ->", end=" ")
                temp = temp.next
            print(temp.info)


s1 = linked_list()

print("Insert At Start:", end=" ")
s1.insert_at_start(20)
s1.insert_at_start(10)
s1.display()

print("Insert At Last:", end=" ")
s1.insert_at_last(30)
s1.insert_at_last(50)
s1.display()

print("Insert At Specific Position:", end=" ")
s1.insert_at_position(40, 3)
s1.display()

print("Insert After Specific Item:", end=" ")
s1.insert_after_specific_item(60, 30)
s1.display()

print("Delete At Start:", end=" ")
s1.delete_start()
s1.display()

print("Delete At Last:", end=" ")
s1.delete_at_last()
s1.display()

print("Delete At Specific Position:", end=" ")
s1.delete_at_position(2)
s1.display()

print("Delete After Specific Item:", end=" ")
s1.delete_after_specific_item(20)
s1.display()