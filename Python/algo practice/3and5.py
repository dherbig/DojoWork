def three_and_five():
	for val in range(100, 4000000):
		div3 = False
		div5 = False
		if val%3 == 0:
			div3 = True
		if val%5 == 0:
			div5 = True
		if not div3 == div5:
			print(val)

three_and_five()
