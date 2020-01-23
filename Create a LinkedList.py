class Node:

  def __init__(self, data):
    self.data= data
    self.next= None

  def printlist(self):
    print(self.data)

class LinkedList:

  def __init__(self):
    self.head= None


if __name__=='__main__': 

  llist= LinkedList()

  llist.head= Node(1)

  llist.head.next= Node(2)

  llist.head.next.next= Node(3)

  llist.head.printlist()
  llist.head.next.printlist()
  llist.head.next.next.printlist()
