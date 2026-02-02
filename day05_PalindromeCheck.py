def PalindromeCheck(string, i=0, rstring=''):
    if i == len(string):
        return rstring
    rstring = string[i] + rstring
    return PalindromeCheck(string, i+1, rstring)

string = str (input("Enter a string to check whether it is palindrome or not : "))
if string == PalindromeCheck(string):
    print("Entered string is palindrome.")
else:
    print("Entered string is not palindrome.")