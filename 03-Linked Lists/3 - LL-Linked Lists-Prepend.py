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
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
    def pop(self):
        if self.length == 0:
            return None
        
        curr = self.head
        pre = self.head
        
        while curr.next:
            pre = curr
            curr = curr.next
            
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return curr.value
    
    def pre(self,value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            
    
my_linked_list = LinkedLists(10)

my_linked_list.append(11)

my_linked_list.pre(9)

my_linked_list.print_list()
            
        
            