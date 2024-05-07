#Encapsulation is the concept of hiding the implementation details of an object from the outside world and only exposing the necessary information through public methods.
class Character:
    def __init__(self, name, weapon, mc, weakness):
        self.name = name
        self.weapon = weapon
        self.__mc = mc
        self__weakness = weakness

    def speak(self, say):
        print(f"{self.name} says {say}")

    def set_damage(self, other, done):
        if other.name = weakness
            dam = dam * 1.25
        weakness = mc - dam
    
    def get_mc(self):
        print self.__mc


Luke = Character("Luke", "Light Saber", 75, "Dad")
DV = Character("Darth Vader", "Light Saber", 125, "Luke")
