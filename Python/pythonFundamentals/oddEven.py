def oddEven(num):
	for count in range(1, num+1):
		oE = ''
		if (count % 2 ==0):
			oE += "even"
		else:
			oE += "odd"
		print ('Number is '+str(count)+'. This is an '+oE+' number.')

oddEven(2000)
