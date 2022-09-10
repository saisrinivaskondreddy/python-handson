def findMissingNumber(lst, n):
   ''' find missing number between
       1 to n integers 
   '''
   sumOfInt = int(n * (n+1) / 2)
   print ("sum of numbers from 1 to n is n*(n+1)/2: ", sumOfInt)
   #currentSum = lst.sum()
   currentSum = sum(lst)
   print ("sum of the numbers from given list is: ", currentSum)
   return sumOfInt-currentSum

def main():
   '''enter a list of number 1 to n, where one number is missing
   '''
   n = int(input("Enter total numbers:"))
   lst = []
   for i in range(0, n-1):
     ele = int(input())
     #lst = lst.append(int(input()))
     lst.append(ele)
   print ("list is", lst)
   missingNum = findMissingNumber(lst, n)
   print ("Missing number fromm the list", missingNum)

if __name__ == "__main__":
   main()
