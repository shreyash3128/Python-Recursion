num = int (input("Enter a number till where you want to want to print: "))
def printNumbers(num, i=1):
    if i > num:
        return
    print(i,end=' ')
    return printNumbers(num, i+1)
printNumbers(num)