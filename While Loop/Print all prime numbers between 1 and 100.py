""" Print all prime numbers between 1 and 100."""

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# Initialize the number to start checking from
number = 1
# Use a while loop to check for prime numbers between 1 and 100
while number <= 100:
    if is_prime(number):
        print(number, end=" ")  # Print the prime number
    number += 1  # Move to the next number
