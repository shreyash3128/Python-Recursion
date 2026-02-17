arr = [7, 0, 5, 8, 2, 0, 4, 1, 2, 5]
min_element = arr[0]   # Assume first element is smallest
i = 1                  # Start from second element

while i < len(arr):
    if arr[i] < min_element:
        min_element = arr[i]
    i += 1

print("Smallest element is:", min_element)