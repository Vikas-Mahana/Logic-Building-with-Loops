""" Calculate the sum of all even numbers from 1 up to n. """


num = int(input("Enter a positive number: "))
# Initialize the variable
n = 1
sum = 0
# Use a while loop to print numbers from 1 to num
while n <= num:
    if n % 2 == 0:
        print(n)
        sum += n
    n +=1 #incremented by 1

print(sum)


