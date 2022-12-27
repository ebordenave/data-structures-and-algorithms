
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
    
my_linked_list = LinkedList(4)

print(f"Head: {my_linked_list.head.value}")
print(f"Tail: {my_linked_list.tail.value}")
print(f"Length: {my_linked_list.length}")



    