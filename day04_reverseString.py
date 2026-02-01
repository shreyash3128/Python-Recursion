def reverseString (string, i = 0, rstring=''):
    if i == len(string):
        return rstring
    rstring = string[i] + rstring
    return reverseString(string, i+1, rstring)
string = str(input("Enter a string : "))
print(f"Reversed of entered sting is {reverseString(string)}")