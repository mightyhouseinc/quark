def base_check(a, y):
    ans = ''
    while a > 0:
        ans += str(a % y)
        a = a // y
    return ans == ans[::-1]


def palindrome(x, base):
    x = str(x)
    if x != x[::-1]:
        return False
    x = int(x)
    x = base_check(x, base)
    x = (str(x))
    return x == x[::-1]


number = 1000000
base = 2
answer = sum(i for i in range(1, number + 1) if palindrome(i, base))
print(answer)
