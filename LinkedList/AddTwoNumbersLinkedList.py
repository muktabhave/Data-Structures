/*https://leetcode.com/problems/add-two-numbers/
Add Two Numbers in LinkedList
*/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        str_l1, str_l2 = '', ''
        while l1:            
            str_l1 += str(l1.val)
            l1 = l1.next
        while l2:            
            str_l2 += str(l2.val)
            l2 = l2.next
        int_l1 = int(str_l1[::-1])
        int_l2 = int(str_l2[::-1])       
        
        l=list(map(int, str(int_l1 + int_l2)[::-1]))
        
        
        tmp= ListNode()
        tmp.val= l[0]
        headnode= tmp
        
        for i in range (1, len(l)):
            
            tmp.next= ListNode(l[i])
            tmp=tmp.next
        
        return headnode
