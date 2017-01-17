y = [5,3,7]

def bubbleSort(l):
    distance = len(l)
    for idx, num in enumerate(l):
        while idx < distance:
            if l[idx] > l[idx+1]:
                (l[idx], l[idx+1]) = (l[idx+1], l[idx])
    print (l)
    return l

bubbleSort(y)
