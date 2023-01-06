class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
class LinkedLists:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        curr = self.head
        pre = self.head
        
        while curr.next is not None:
            pre = curr
            curr = curr.next
            
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return curr


my_linked_list = LinkedLists(1)

my_linked_list.append(2)

my_linked_list.pop()

my_linked_list.print_list()            