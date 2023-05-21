class Node:

  def __init__(self,data):
    self.data=data
    self.next=None


class LinkedList:

  def __init__(self):  # create a top as starting and storing the address of all the element of LL
    self.top=None


  def insert_at_begin(self,data):
    node=Node(data)                 #creating a node(data=value, next=None)

    if self.top is None:
      self.top=node                
    else:
      print("First element is inserted!!")
      return                       

  def insert(self,data):
    node=Node(data)
    current_node=self.top
    if current_node.next is   :   
      current_node.next=node
    else:
      while(current_node.next is not None):
        current_node=current_node.next   
      current_node.next=node          

  def insert_at_end(self,data):
    node=Node(data)

    current_node=self.top

    while current_node.next is not None:
      current_node=current_node.next
    current_node.next=node

  # pop the element 

  def pop(self,data):
    current_node=self.top

    if current_node.data==data:
      self.top=current_node.next

    else:

      while current_node is not None:

        if current_node.data==data:
          break

        prev=current_node
        current_node=current_node.next

      if current_node == None:
        return
      prev.next = current_node.next
      current_node = None

  def printEle(self):

    current_node=self.top

    while current_node is not None:
      print(current_node.data)
      current_node=current_node.next
      

if __name__ == '__main__':
  ll=LinkedList()
  ll.insert_at_begin(2)
  ll.insert_at_begin(3)
  ll.insert(5)
  ll.insert(4)
  ll.pop(1)
  ll.insert(1)
  ll.printEle()

