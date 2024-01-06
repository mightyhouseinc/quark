## Part of Cosmos by OpenGenus Foundation
## Find of average of numbers in an array
## Contributed by: Pranav Gupta (foobar98)

n = int(input("Enter no. of elements: "))
a = []  # empty list

for _ in range(0, n):
    # every number in a new line
    x = int(input("Enter number: "))
    a.append(x)

avg = sum(a) / n
print(f"Average of numbers in list: {str(round(avg, 2))}")
