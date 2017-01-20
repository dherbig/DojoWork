class Bike (object):
    def __init__(self, speed, price=0):
        self.price = price
        self.speed = speed
        self.miles = 0
    def displayInfo(self):
        print ("This bike cost $%d, goes %d MPH, and has traveled %d miles.") % (self.price, self.speed, self.miles)
    def ride(self):
        print ('Riding...')
        self.miles += 10
        return self
    def reverse(self):
        print ('Reversing...')
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

fixie = Bike(4, 300)
fixie.ride().ride().ride().reverse().displayInfo()

recumbent = Bike(20, 900)
recumbent.ride()
recumbent.ride()
recumbent.reverse()
recumbent.reverse()
recumbent.displayInfo()

clownBike = Bike(10, 1000)
clownBike.reverse()
clownBike.reverse()
clownBike.reverse()
clownBike.displayInfo()
