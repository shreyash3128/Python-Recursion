string = input("Enter a string: ")

count = 0
index = 0

while string[index:index+1] != "":
    count += 1
    index += 1

print("Length of string is:", count)