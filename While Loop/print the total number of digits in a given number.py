""" Count and print the total number of digits in a given number. """

num = int(input("Enter a positive number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Total number of digits:", count)