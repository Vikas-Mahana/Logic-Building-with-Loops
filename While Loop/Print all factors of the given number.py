"""Print all factors of the given number."""
n = 12
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1