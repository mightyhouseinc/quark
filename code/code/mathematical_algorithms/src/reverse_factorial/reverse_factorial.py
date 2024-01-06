# Part of Cosmos by OpenGenus Foundation
def reversefactorial(factorial):
    n = 1
    m = 0
    notfound = True
    while m <100:
        m += 1
        n *= m
        if factorial == n:
            print(f"{str(factorial)} is {m}!")
            notfound = False
            break
        elif m == 100:
            print(f"{str(factorial)} is not a factorial product of any integer.")

factorial = int(input("Reverse Factorial > "))
reversefactorial(factorial)
