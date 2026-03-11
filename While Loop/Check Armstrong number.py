""" Check whether the given number is an Armstrong number or not. """

# Get the number from the user
number = int(input("Enter a number to check if it is an Armstrong number: "))

# Initialize variables
original_number = number
armstrong_sum = 0
num_digits = len(str(number))  # Get the number of digits in the number
# Use a while loop to calculate the sum of the digits raised to the power of the number of digits
while number > 0:
    digit = number % 10  # Get the last digit
    armstrong_sum += digit ** num_digits  # Add the digit raised to the power of num_digits to the sum
    number //= 10  # Remove the last digit
# Check if the calculated sum is equal to the original number
if armstrong_sum == original_number:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")
