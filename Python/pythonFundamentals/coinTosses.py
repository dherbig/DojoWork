import random
headCount = 0
tailCount = 0
flipCount = 0
for i in enumerate(range(1, 5001)):
    response = ''
    flip = round(random.random())
    flipCount += 1
    response += "Attempt #" + str(flipCount) + ": Throwing a coin... It's a "
    if flip == 0:
        headCount += 1
        response += "head"
    else:
        tailCount += 1
        response += "tail"
    response += "! ... Got " + str(headCount) + "head(s) so far and " + str(tailCount) + "tail(s) so far"
    print(response)
print ("Ending the program, thank you!")
