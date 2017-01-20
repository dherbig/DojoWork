class Animal(object):
    def __init__(self, name):
        self.health = 100
        self.name = name

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print (str(self.name) + ' has ' + str(self.health) + " HP remaining.")
        return self

aminal = Animal('Animal')
aminal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

pupper = Dog('Fido')
pupper.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def displayHealth(self):
        print ("I'm a dragon!")
        super(Dragon, self).displayHealth()

    def fly(self):
        self.health -= 10
        return self

NicolBolas = Dragon('Nico')
NicolBolas.walk().walk().walk().run().run().fly().fly().displayHealth()

aminal.fly()
