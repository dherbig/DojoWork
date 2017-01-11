print ("Scores and Grades")
for i in range(1, 11):
	print ('So, what score did you get? Out of 100?')
	score = input();
	if score > 90:
		print ('Score: ' + str(score) + '; Your grade is an A!')
	elif score > 80:
		print ('Score: ' + str(score) + '; Your grade is an B!')
	elif score > 70:
		print ('Score: ' + str(score) + '; Your grade is an C!')
	elif score > 60:
		print ('Score: ' + str(score) + '; Your grade is an D...')
	else:
		print ('Score: ' + str(score) + '; You should have done your homework!')
print ('End of the program. Bye!')
