class Node:
  '''
  linkedlist Node
  '''
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  '''
  Linkedlist Representation
  '''
  def __init__(self):
    self.head = None

  # print contents of linked list
  def printList(self):
      temp = self.head
      while (temp):
         print(temp.data)
         temp = temp.next

  def addBegin(self, data):
      new = Node(data)
      new.next = self.head
      self.head = new

  def addLast(self, data):
      new = Node(data)
      last = self.head
      while (last.next):
         last = last.next
      last.next = new

  def length(self):
      length = 0
      current = self.head
      while (current):
         length += 1
         current = current.next  
      return length

if __name__ == '__main__':
  llist = LinkedList()
  llist.head = Node(1)
  second = Node(2)
  third = Node(3)

  llist.head.next = second
  #llist.second.next = third
  second.next = third

  print ("print linkedlist data")
  llist.printList()
 
  print ("\nprint linkedlist data with new Begin")
  llist.addBegin(5)
  llist.printList()
  
  print ("\nprint linkedlist data with new Last")
  llist.addLast(2)
  llist.printList()

  print ("linked list", llist)
  print ("linked list head", llist.head)
  print ("linked list head data", llist.head.data)

  print ("length of linked list: ", llist.length())
