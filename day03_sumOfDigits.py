num = int(input("enter a number : "))
sum = 0
while num > 0:
    x = num % 10
    sum += x
    num //= 10
print (f"Sum of the digits of entered number is : {sum}")