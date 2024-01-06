import math

# pascals_tri_formula = 
print "Enter a number : "
inp=input()

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y): # don't see where this is being used...
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    result = [] # need something to collect our results in
    # count = 0 # avoidable! better to use a for loop, 
    # while count <= rows: # can avoid initializing and incrementing
    for count in range(rows): # start at 0, up to but not including rows number.
        row = [combination(count, element) for element in range(count + 1)]
        result.append(row)
            # count += 1 # avoidable
    return result

# now we can print a result:
for row in pascals_triangle(inp):
    print(row)