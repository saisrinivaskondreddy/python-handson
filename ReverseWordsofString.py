def reverseWords(ss):
    #for i in ss.split():
    ssLst = []
    ssLst = ss.split()
    print ("string is of length: ", len(ssLst))
    for i in reversed(range(len(ssLst))):
        #print(ssLst[i], sep=' ')
        print(ssLst[i], end=' ')
    return None

def main():
   '''
   main function
   Program to print the words in reverse of a sentense. Example below
   input: This is my first string program
   output: program string first my is This
   '''
   ss = input("Enter a string: ")
   reverseWords(ss)
   print("\n")

if __name__ == "__main__":
   main()
