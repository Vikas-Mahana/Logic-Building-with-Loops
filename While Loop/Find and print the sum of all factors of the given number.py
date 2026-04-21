"""Find and print the sum of all factors of the given number."""

def sum_of_factors(n):
    total = 0
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            
            # Add the corresponding pair factor
            if i != n // i:
                total += n // i
                
    return total


# Input from user
num = int(input("Enter a number: "))
result = sum_of_factors(num)

print(f"Sum of all factors of {num} is: {result}")