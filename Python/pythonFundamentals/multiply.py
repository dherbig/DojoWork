def multiply(orig, num):
	for count in range(len(orig)):
		orig[count] *= num
	return orig
a = [2,4,10,16]
b = multiply(a,5)
print (b)
