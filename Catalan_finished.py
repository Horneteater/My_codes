#program to calculate 6 numbers in catalan sequence

import math

for i in range(6):
	c=(math.factorial((2*i)))/(((math.factorial(i+1)))*math.factorial(i))
	print(c)