def reverseStr(myS):
    for i in range(len(myS)-1, -1, -1):
        print (myS[i], end='')

def main():
    '''
    script to reverse a given string
    '''
    myStr = input("Enter a string: ")
    reverseStr(myStr)
    print("\n")

if __name__ == "__main__":
   main()
