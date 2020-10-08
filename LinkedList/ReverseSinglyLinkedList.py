class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev= None
        current= head
        
        while(current!= None):
            
            next=current.next
            
            current.next= prev
            
            prev= current
            current=next
            
        head= prev
        return head
        
