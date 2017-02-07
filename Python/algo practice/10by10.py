from random import choice
def x10grid():
	for number in range(10):
		row = ''
		for count in range(10):
			opt = ['D',"E"]
			x = choice(opt)
			row += x
		print (str(row))


x10grid()
