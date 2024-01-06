print ("Amicable Numbers below 10000 are:")
for m in range(1,10000):
    x=m
    sum1 = sum(i for i in range(1,x) if x%i==0)
    y=sum1
    sum2 = sum(j for j in range(1,y) if y%j==0)
    if(sum2==x) and (x!=y):
        print(x)
