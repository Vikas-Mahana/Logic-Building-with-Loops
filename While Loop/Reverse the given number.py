""" Reverse the given number and print the reversed value. """

num = int(input("Enter a number that can reverse: "))
reverse = 0
while num > 0:
    last_num = num %  10
    reverse = reverse * 10 + last_num
    num //= 10 # remove last digit
print(reverse)
