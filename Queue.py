class Queue:

    def __init__(self,cap):
        self.items= [None]*cap
        self.cap= cap
        self.front= -1
        self.rear= -1
    
    def IsEmpty(self):
        if (self.front==self.rear==-1):
            return True
      
    def IsFull(self):
        if ( self.front==(self.rear+1)%self.cap ):
            return True

    def enqueue(self, data):
        if (self.IsFull()== True):
            print ('Queue is full, cant insert items') 
            
        else:
            self.rear=(self.rear+1)%self.cap
            self.items[self.rear]= data 
            if (self.front==-1):
                self.front=0
    
    def dequeue(self):
        if (self.IsEmpty()== True):
            print ('Queue is Empty, cant delete items')
        elif (self.front==self.rear):
            self.front=self.rear=-1 
        else:
            self.front=(self.front+1)%self.cap
        #print(self.front, self.rear)
    
    def printqueue(self):
        #print(self.items)
        i=self.front
        while(i<=self.rear):
            print(self.items[i])
            i+=1
    
if __name__=='__main__':         
    qu=Queue(3)
    
    qu.enqueue(2)
    qu.enqueue(3)
    qu.enqueue(6)
    
    qu.printqueue()
    
    qu.dequeue()
    qu.printqueue()
    