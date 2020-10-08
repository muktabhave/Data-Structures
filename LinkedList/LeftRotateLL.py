class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head= None
    
    #push element at end
    def pushll(self,ele):
        #if LL is empty
        if(self.head== None):
            self.head= Node(ele)
        
        else:
            tmp= self.head
            
            while(tmp.next!=None):
                tmp=tmp.next
            
            tmp.next=Node(ele)
    
    def rotatell(self,k):
        
        if (k==0):
            return
        
        tmp=self.head
        
        i=1
        
        while (i<k and tmp is not None):
            
            tmp=tmp.next
            i=i+1
        
        if (tmp is None):
            return
            
        kthnode=tmp
        
        
        while(tmp.next is not None):
            
            tmp=tmp.next
        
        tmp.next=self.head
        
        self.head=kthnode.next
        
        kthnode.next=None
        
    
    def printll(self):
        
        if(self.head== None):
            print("List is empty")
        else:
            tmp=self.head
            while(tmp!=None):
                print(tmp.data)
                tmp=tmp.next
                
        
if (__name__=='__main__'):
    
    ll= LinkedList()
    ll.pushll(10)
    ll.pushll(20)
    ll.pushll(30)
    ll.pushll(40)
    ll.pushll(50)
    # ll.printll()
    ll.rotatell(2)
    ll.printll()
    
