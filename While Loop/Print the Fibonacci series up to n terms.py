""" Print the Fibonacci series up to n terms"""

# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b  # Update to the next two Fibonacci numbers
        count += 1  # Increment the count
# Get user input for the number of terms
n_terms = int(input("Enter the number of terms: "))
# Call the function to print the Fibonacci series
fibonacci(n_terms)

