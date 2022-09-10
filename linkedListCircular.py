class Node:
  def __init__(self, value):
     self.data = value
     self.next = None

class LinkedList():
  def __init__(self):
     self.head = None

  def addBegin(self, data):
     temp = Node(data)
     temp.next = self.head
     self.head = temp

  def findLoop(self):
     ''' 
     store hash address of each node in python set
     '''
     myset = set()

     temp = self.head
     while (temp):
        if (temp in myset):
           return True
        
        print ("node address", temp) 
        myset.add(temp)
        temp = temp.next

     return False

  def printList(self):
      current = self.head
      while (current):
         print (current.data)
         current = current.next

def main():
   myList = LinkedList()
   myList.head = Node(5)
   second = Node(8)
   third = Node(4)
   myList.head.next = second
   second.next = third   
   third.next = Node(8)
   third.next.next = Node(4)
   thrid.next.next = third
   
   myList.printList() 
   
   if (myList.findLoop()):
      print ("Loop Found")
   else:
      print ("Loop not Found")

if __name__ == '__main__':
   main()
