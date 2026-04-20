"""Print all numbers between a and b that are divisible by 7."""
a = 1
b = 100
i = a
while i <= b:
    if i % 7 == 0:
        print(i)
    i += 1