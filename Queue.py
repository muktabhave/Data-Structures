class Queue:

	def __init__(self,capacity):
		self.items= [None]*capacity
		self.size= len(self.items)
		self.front= -1
		self.rear= self.size-1
	
	def IsEmpty(self):
		if (self.size==0):
			return True
      
	# def IsFull(self):
	# 	if (items[(self.rear+1)%size]):
	# 		return True

	# def Enqueue(self, data):
	# 	if IsFull():
	# 		print (“que is full”)
    #         return
    #     else:
	# 	    rear=(rear+1)%size
	# 	    items[rear]= data

	# def deQueue:
	# 	if IsEmpty():
	# 		print (“Que is Empty”)
    #         return
    #     else:
	# 	front=(front+1)%size
	
if __name__=='__main__': 		
    qu=Queue()

# qu.Enqueue(2)
# qu.Enqueue(3)
# qu.Enqueue(6)
# qu.Enqueue(5)
# qu.deQueue()
    qu.items=[2,3]

    print (qu.size)
    print (qu.front)
    print (qu.rear)
    if (qu.IsEmpty()==True):
        print("True")
    else:
        print("False")
# print(qu.items)

