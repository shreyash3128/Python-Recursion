

def fibonacci_recursive(n, a=0, b=1):
    # Base Case: Stop when n reaches 0
    if n <= 0:
        return
    
    # Print the current number
    print(a, end=" ")
    
    # Recursive Step: 
    # The new 'a' becomes the old 'b'
    # The new 'b' becomes 'a + b'
    fibonacci_recursive(n - 1, b, a + b)

# Get input and call the function
num = int(input("Enter a number: "))
fibonacci_recursive(num)