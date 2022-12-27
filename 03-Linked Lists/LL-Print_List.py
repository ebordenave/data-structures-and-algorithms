class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        # create a new node
        new_node = Node(value)
        
        # start with condition where data structure is empty
        # head and tail pointers will point to the same node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    def pop(self):
        # check if list is empty
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        
        # assign pre to be node previous to tail using this
        while temp.next:
            pre = temp
            temp = temp.next
            
        # tail will now equal previous node
        # next point will be none
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        # edge case handling
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self):
        # check if list is empty
        if self.length == 0:
            return None
        
        
            
    
            
my_linked_list = LinkedList(11)
my_linked_list.append(3)

# (2) Items - Returns 1 Node
print(my_linked_list.pop())

# (1) Items - Returns 1 Node
print(my_linked_list.pop())

# (0) Items - Returns None
print(my_linked_list.pop())



    
        

