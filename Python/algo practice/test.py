import time

#use time.time() on Linux

start = time.clock()

for x in range(1000):
    pass
stop = time.clock()

print stop-start

start = time.clock()
for x in xrange(1000):
    pass
stop = time.clock()

print stop-start
