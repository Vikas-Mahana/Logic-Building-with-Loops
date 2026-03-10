""" Find and print the sum of digits of the given number. """

# Get the number from the user
number = int(input("Enter a number to find the sum of its digits: "))
# Initialize the sum variable
sum_of_digits = 0
# Use a while loop to calculate the sum of digits
while number > 0:
    digit = number % 10  # Get the last digit
    sum_of_digits += digit  # Add the digit to the sum
    number //= 10  # Remove the last digit

# Print the sum of digits
print("The sum of digits of the given number is:", sum_of_digits)