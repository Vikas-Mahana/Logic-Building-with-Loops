""" Print the multiplication table of a given number from n × 1 to n × 10. """


# Get the number from the user
number = int(input("Enter a number to print its multiplication table: "))
# Initialize the multiplier
multiplier = 1
# Use a while loop to print the multiplication table
while multiplier <= 10:
    result = number * multiplier
    print(f"{number} × {multiplier} = {result}")
    multiplier += 1  # Increment the multiplier by 110
