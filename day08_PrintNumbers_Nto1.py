num = int (input("Enter a number from where you want to want to print: "))
def printNumbers(num):
    if num < 1:
        return
    print(num,end=' ')
    return printNumbers(num-1)
printNumbers(num)

print()
def printNum(num):
    for i in range(num, 0, -1):
        yield i
print(list(printNum(num)))