"""  Calculate and print the sum of the first n natural numbers."""

# Get the number of natural numbers to sum from the user
n = int(input("Enter a positive integer to calculate the sum of the first n natural numbers: "))
# Initialize the sum variable   
total_sum = 0
# Initialize the counter
counter = 1
# Use a while loop to calculate the sum
while counter <= n:
    total_sum += counter  # Add the current counter value to the total sum
    counter += 1  # Increment the counter by 1

# Print the result
print(f"The sum of the first {n} natural numbers is: {total_sum}")