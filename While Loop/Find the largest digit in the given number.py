"""Find the largest digit in the given number."""

def largest_digit(n):
    n = abs(n)  # Handle negative numbers
    max_digit = 0

    while n > 0:
        digit = n % 10
        if digit > max_digit:
            max_digit = digit
        n //= 10

    return max_digit


# Input from user
num = int(input("Enter a number: "))

# Special case if number is 0
if num == 0:
    print("Largest digit is: 0")
else:
    print("Largest digit is:", largest_digit(num))