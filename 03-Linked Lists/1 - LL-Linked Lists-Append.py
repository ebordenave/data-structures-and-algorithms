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
        while curr is not None:
            print(curr.value)
            curr = curr.next
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
            
my_linked_list = LinkedLists(4)

my_linked_list.append(4)

my_linked_list.print_list()