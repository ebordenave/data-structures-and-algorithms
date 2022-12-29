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
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1  
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return temp.value
        return False
        
        
        
        
            
            
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
# my_linked_list.prepend(1)

# my_linked_list.pop()

# my_linked_list.pop_first()

# my_linked_list.set_value(1,11)

my_linked_list.print_list()



    
        

