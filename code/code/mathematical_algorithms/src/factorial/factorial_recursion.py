# Part of Cosmos by OpenGenus Foundation
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

n = int(input("Enter a number"))
print(f"The factorial is {str(factorial(n))}")
