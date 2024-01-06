def catalanNum(n):
    if n <=1 :
        return 1

    return sum(catalanNum(i) * catalanNum(n-i-1) for i in range(n))
 
for i in range(15):
    print catalanNum(i)