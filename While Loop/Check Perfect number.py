""" Check whether the given number is a Perfect number. """

# Get the number from the user
number = int(input("Enter a number to check if it is a Perfect number: "))
# Initialize variables
original_number = number
divisor_sum = 0

# Use a while loop to calculate the sum of proper divisors
divisor = 1
while divisor < original_number:
    if original_number % divisor == 0:  # Check if it is a proper divisor
        divisor_sum += divisor  # Add the divisor to the sum
        print(f"Divisor: {divisor}, Current Sum of Divisors: {divisor_sum}")  # Print the current divisor and sum
    divisor += 1  # Move to the next potential divisor
# Check if the calculated sum of divisors is equal to the original number
if divisor_sum == original_number:
    print(f"{original_number} is a Perfect number.")
else:
    print(f"{original_number} is not a Perfect number.")
