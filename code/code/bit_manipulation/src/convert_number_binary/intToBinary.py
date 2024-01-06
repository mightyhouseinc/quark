#part of Cosmos by OpenGenus Foundation

import math

def intToBinary(i):
	if i == 0: return "0"
	s = ''
	while i:
		s = f"1{s}" if i % 2 == 1 else f"0{s}"
		i /= 2
	return s

#sample test
n = 741
print(intToBinary(n))
