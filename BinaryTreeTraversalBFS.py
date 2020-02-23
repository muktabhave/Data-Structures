class Node:
    
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    
if (__name__=='__main__'):
    
    root=Node(10)
    root.left= Node(20)
    root.right=Node(5)
    root.left.left=Node(3)
    root.left.right=Node(30)
    
    def bfs(n):
        
        q=[]
        q.append(n)
        while(len(q)>0):
            
            ele=q.pop(0)
            print(ele.data)
            if (ele.left!= None):
                q.append(ele.left)
            if(ele.right!=None):
                q.append(ele.right)                   
    
    bfs(root)
