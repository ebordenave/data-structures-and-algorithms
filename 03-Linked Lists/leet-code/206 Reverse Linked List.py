class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
class Solution:
    def __init__(self, value):
        new_node = ListNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        cur = self.head
        while (cur.next != None):
            print(cur.value)
            cur = cur.next
            
    def reverse(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        