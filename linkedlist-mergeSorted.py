class Node:
  '''
  Node Definetion
  '''
  def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
  '''
  Linkedlist definition class
  '''
  def __init__(self):
      self.head = None

  def append(self, new_value):
      temp = Node(new_value)
      if self.head == None:
         self.head = temp
         return
      
      current = self.head
      while (current.next != None):
            current = current.next
      current.next = temp
            
  def mergeSort(self):
      # a : ascending order
      print ("place for merge sort")
      current = self.head
      if (current == None or current.next == None):
         return current
     
      left = self.mergeSort(current, self.findMiddle)
      right = self.mergeSort(self.findMiddle.next) 
      sortedList = self.mergeSortedList(left, right)
  
  def mergeSortedList(self, ll1, ll2):
      result = None
      print ("merge of lists here")
      a = ll1.head
      b = ll2.head
      if (a.data == None):
         return b
      elif (b.data == None):
         return a
      if (a.data <= b.data):
         result = a
         result.next = self.mergeSortedList(a.next, b)
      else:
         result = b
         result.next = self.mergeSortedList(a, b.next)

  def findMiddle(self):
      totalCount = findCount()
      print ("length of linked list is: ", totalCount)
      return int(totalCount/2)
      
  def findCount(self):
      count=0
      current = self.head
      while (current):
          count += 1
          current = current.next
 
  def printList(self):
      current = self.head
      while (current):
         print(current.data)
         current = current.next

def main():
  lst = LinkedList()
  lst.append(10)
  lst.append(9)
  lst.append(3)
  lst.append(12)
  lst.printList()
  
  lst.mergeSort()
  lst.printList()
 
if __name__ == '__main__':
   main ()
  
