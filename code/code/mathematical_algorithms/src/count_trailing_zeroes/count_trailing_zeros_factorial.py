# Part of Cosmos by OpenGenus Foundation
def findTrailingZeroes(n):
	count = 0
	i=5
	while (n//i>=1):
		count = count + n//i
		i *= 5
	return count
n = int(input("Enter the number:"))
print(f"You entered {n}")
print(f"The number of trailing zeroes = {str(findTrailingZeroes(n))}")
