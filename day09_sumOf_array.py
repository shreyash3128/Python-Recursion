# Use split() to catch numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")
array = user_input.split()
print(user_input)

i = 0
total_sum = 0 # Renamed 'sum' because sum() is a built-in Python function

while i <= len(array) - 1:
    # Convert the string element to an integer before adding
    total_sum += int(array[i])
    i += 1

print("The sum is:", total_sum)