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
    
    def popll(self,ele):
        #if list is empty
        if(self.head== None):
            print("list is empty, cant delete ele")
        
        else:
            tmp=self.head
            
            if (tmp.data==ele):
                self.head=tmp.next
            else:
                
                while(tmp.next.data!=ele and tmp!=None):
                    tmp=tmp.next
            
                if (tmp==None):
                    print("Node to be deleted not found")
                else:
                    tmp.next=tmp.next.next
    
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
    ll.printll()
    
    ll.popll(30)
    ll.printll()   
    ll.popll(10)
    ll.printll()
    ll.popll(20)
    ll.printll()
    ll.popll(10)
    
