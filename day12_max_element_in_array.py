arr = [7, 0, 5, 8, 2, 0, 4, 1, 2, 5]
min_element = arr[0]   # Assume first element is smallest
i = 1                  # Start from second element

while i < len(arr):
    if arr[i] < min_element:
        min_element = arr[i]
    i += 1

print("Smallest element is:", min_element)

# Recursive function to find smallest element

def find_min(arr, n):
    # Base condition
    if n == 1:
        return arr[0]
    
    min_of_rest = find_min(arr, n-1)
    
    if arr[n-1] < min_of_rest:
        return arr[n-1]
    else:
        return min_of_rest


arr = [10, 45, 23, 89, 12, 67]

print("Smallest element is:", find_min(arr, len(arr)))
