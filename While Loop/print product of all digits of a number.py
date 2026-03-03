""" Find and print the product of all digits of a given number. """

num = int(input("Enter a number: "))

product = 1
# Make number positive (in case user enters negative number)
num = abs(num)
while num > 0:
    digit = num % 10      # get last digit
    product *= digit      # multiply with product
    num //= 10            # remove last digit

print("Product of digits is:", product)