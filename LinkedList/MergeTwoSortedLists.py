# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        newhead=ListNode(0)
        
        tmp=newhead
        
        while (True):

            while (l1!=None and l2!=None): 
                
                if(l1.val<l2.val):
                    tmp.next=l1
                    l1= l1.next
            
                else:
                    tmp.next=l2
                    l2=l2.next
            
                tmp=tmp.next
        
            if (l1 is None):
            
                tmp.next=l2
                break
            if (l2 is None):
            
                tmp.next=l1
                break  
        
        return (newhead.next)
        
    
        
        
