def sumOfDigits (num, sum=0):
    if num <= 0:
        return sum
    a = num % 10 
    sum += a
    return sumOfDigits(num//10, sum)
num = int(input("enter a number : "))
print (f"Sum of the digits of entered number is : {sumOfDigits(num)}")