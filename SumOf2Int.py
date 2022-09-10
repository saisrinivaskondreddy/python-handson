def findSumOf2Int(lst, n, sum):
  '''
  find 2 numbers whose addition make to sum
  '''
  j = 0
  matchFound = "false"
  for i in range(0, n):
    for j in range(i+1, n):
      if lst[i] + lst[j] == sum:
         print ("sum of " + str(lst[i]) + " and " + str(lst[j]) + " is: " + str(sum))
         matchFound = "true"
      else:
         continue
  if matchFound == "false":
     print ("No two integers sum upto: ", sum)
      


def main():
  '''
  find the numbers whose sum is equal to the number given from the list of numbers
  '''
  lst = []
  n = int(input("Enter total numbers: "))
  for i in range(0, n):
    ele = int(input())
    lst.append(ele)
  
  value = int(input("Enter the sum of 2 int to check: "))
  findSumOf2Int(lst, n, value)

if __name__ == "__main__":
  main()
