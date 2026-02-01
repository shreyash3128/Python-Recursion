string = str(input("Enter a string : "))
rstring = ''
i = 0
while i <= len(string)-1:
    rstring = string[i] + rstring
    i += 1

print(f"Reversed of entered sting is {rstring}")