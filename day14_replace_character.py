# Replace character using while loop

string = input("Enter a string: ")
old_char = input("Enter character to replace: ")
new_char = input("Enter new character: ")

result = ""
i = 0

while i < len(string):
    if string[i] == old_char:
        result = result + new_char
    else:
        result = result + string[i]
    i += 1

print("Updated string:", result)