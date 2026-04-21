"""Find the HCF (Highest Common Factor) of two given numbers."""

def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = find_hcf(num1, num2)
print(f"HCF of {num1} and {num2} is: {hcf}")