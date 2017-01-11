def draw_stars(list):
    #For every value in the list that is passed,
    for val in list:
        #reset the output string
        out = ''
        #If it's a number,
        if val >= 0 and val <=9:
            #add a star to our output string.
            for x in range(1, val+1):
                out += '*'
        #If it's a word,
        else:
            #find the first letter of that word
            fL = val[0].lower()
            #and add it to the output string a number of times equal to it's length.
            for x in range(1, len(val)+1):
                out += fL
        #Print the output string
        print (out)

p = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(p)
