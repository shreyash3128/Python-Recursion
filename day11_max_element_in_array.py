def find_max_recursive(arr, n):
    if n == 1:
        return arr[0]
    
    return max(arr[n-1], find_max_recursive(arr, n-1))

numbers = [15, 27, 3, 99, 42]
result = find_max_recursive(numbers, len(numbers))
print(f"The largest element is: {result}")