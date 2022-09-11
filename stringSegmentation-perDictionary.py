def findSubString(word, myDict):
  for i in range(0, len(word)+1):
      firstWord = word[0:i]
      if firstWord in myDict:
         secondWord = word[i:]
         print("firstword match: ", firstWord, "secondWord to match: ", secondWord )
         if secondWord in myDict or secondWord == None or findSubString(secondWord, myDict):
            print (firstWord, secondWord)
            return True
  return False

def main():
  myDict = set(['apple', 'peer', 'cider', 'venigar', 'pie'])
  segString = input("Enter a string: ")
  print(segString)
  if findSubString(segString, myDict):
     print ("String can segmented")
  else:
     print ("Stirng can not be segmented")

  
if __name__ == "__main__":
  main()
