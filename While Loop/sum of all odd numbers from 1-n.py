""" Calculate the sum of all odd numbers from 1 up to n. """

num = int(input("Enter a positive number: "))
n = 1
sum = 0
while n <= num:
    if n % 2 != 0:
        print(n)
        sum += n
    n +=1 #incremented by 1
print(sum)
