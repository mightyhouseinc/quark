def safePos(n, k):
    return 0 if n == 1 else (safePos(n - 1, k) + k) % n


n = int(input("Enter the number of people : "))
k = int(input("Enter the kth value of people getting executed : "))
print("The Safe position to stand is",
      safePos(n, k) + 1)  # Answer is for 1 based indexing
