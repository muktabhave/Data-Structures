class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
        self.prev=None
        
class LinkedList:
    def __init__(self):
        self.head= None
    
    #push ele at last position
    
    def pushll(self, ele):
        if(self.head==None):
            self.head=Node(ele)
        
        else:
            tmp=self.head
            while(tmp.next!=None):
                tmp=tmp.next
            tmp.next=Node(ele)
            Node(ele).prev= tmp
    
    def printll(self):
        
        tmp=self.head
        while(tmp!= None):
            print (tmp.data)
            tmp=tmp.next
    
    def popll(self, ele):
        if(self.head==ele):
            self.head=self.head.next
            self.head.prev=None
        else:
            tmp=self.head
            
            while(tmp.data!=ele and tmp!=None):
                tmp=tmp.next
            if(tmp.data==None):
                print("Node to be deleted is not in list")
            else:
                tmp.prev.next=tmp.next
                tmp.next.prev=tmp.prev
        
if (__name__=='__main__'):
    
    ll=LinkedList()
    
    ll.pushll(10)
    
    ll.printll()
                
    ll.pushll(20)
    
    ll.pushll(30)
    
    ll.printll()
    
    ll.popll(10)
    
    ll.printll()
