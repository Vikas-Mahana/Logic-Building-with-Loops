""" Check whether the given number is a palindrome. """

num = int(input("Enter a number to check palindrome or not: "))
temp = str(num)
if num == int(temp[::-1]):
    print("It is a palindrome number.")
else:
    print("It is not a palindrome number.")