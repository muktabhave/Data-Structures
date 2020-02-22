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
    
    def dfs_preorder(n):
        if(n!=None):
            print(n.data)
            dfs_preorder(n.left)
            dfs_preorder(n.right)
    
    dfs_preorder(root)

    def dfs_inorder(n):
        if(n!=None):
            dfs_inorder(n.left)
            print(n.data)
            dfs_inorder(n.right)
    
    dfs_inorder(root)
    
    def dfs_postorder(n):
        if(n!=None):
            dfs_postorder(n.left)
            dfs_postorder(n.right)
            print(n.data)
    
    dfs_postorder(root)
