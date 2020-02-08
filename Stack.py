class Stack:
    def __init__(self, cap):
        self.cap=cap
        self.top=-1
        self.items=[None]*self.cap

    def isempty(self):
        if(self.top==-1):
            return True
    
    def isfull(self):
        if(self.top==self.cap-1):
            return True

    def findtop(self):
        return self.items[self.top]
    
    def push(self, data):
        if(self.isfull()== True):
            print ("stack is full")
        else:
            self.top=self.top+1
            self.items[self.top]= data

    def pop(self):
        if(self.isempty()== True):
            print('stack is empty')
        else:
            self.top=self.top-1
    
    def printstack(self):
        i=0
        while (i <=self.top):
            print (self.items[i])
            i+=1

if __name__=='__main__': 
    st= Stack(5) #create an object st of stack class

    st.push(10)

    # st.printstack()

    st.push(20)

    st.pop()

    st.push(30)

    # st.printstack()

    st.push(40)

    st.push(50)

    st.push(60)

    st.printstack()

    st.push(20)
