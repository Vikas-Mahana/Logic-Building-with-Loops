""" Calculate and print the factorial of a given number. """

# Get input from user.
num = int(input("Enter a positive number: "))
fact = 1
# Use a while loop for factorial number
while 1 < num:
    # print(num, end=" ")
    fact *= num
    num -= 1
print(fact)