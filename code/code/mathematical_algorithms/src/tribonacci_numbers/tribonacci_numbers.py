n=int(input())
a = [0, 0, 1]
a.extend(a[i-1]+a[i-2]+a[i-3] for i in range(3,n))
for i in a:
	print(i)