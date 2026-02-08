num = int (input("Enter a number from where you want to want to print: "))
def printNumbers(num):
    if num < 1:
        return
    print(num,end=' ')
    return printNumbers(num-1)
printNumbers(num)