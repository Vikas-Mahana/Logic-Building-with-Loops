"""Find the smallest digit in the given number"""

def smallest_digit(n):
    n = abs(n)  # Handle negative numbers
    min_digit = 9

    while n > 0:
        digit = n % 10
        if digit < min_digit:
            min_digit = digit
        n //= 10

    return min_digit


# Input from user
num = int(input("Enter a number: "))

# Special case if number is 0
if num == 0:
    print("Smallest digit is: 0")
else:
    print("Smallest digit is:", smallest_digit(num))