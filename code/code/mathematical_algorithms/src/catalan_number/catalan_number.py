# Part of Cosmos by OpenGenus Foundation

def catalan(n):
    
    return 1 if n <=1 else sum(catalan(i) * catalan(n-i-1) for i in range(n))
 

for i in range(10):
    print catalan(i),

