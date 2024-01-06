n = int(input("Enter number of elements:"))
elements = [int(input("Enter element:")) for _ in range(0, n)]
elements.sort()
print("Largest element is : ", elements[n - 1])
