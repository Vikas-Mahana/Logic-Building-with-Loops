""" Check whether the given number is a prime number """
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# Get user input
number = int(input("Enter a number: "))
# Use a while loop to check if the number is prime
while True:
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    break  # Exit the loop after checking the number
