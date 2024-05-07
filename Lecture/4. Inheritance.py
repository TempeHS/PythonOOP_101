# Inheritance is a mechanism that allows a class to inherit properties and methods from another class, called the superclass or parent class.
class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon


class Has_Script(Character):
    def __init__(self, name, weapon, mc, side):
        super().__init__(name, weapon)
        self.mc = mc
        self.side = side

    def speak(self, say):
        print(f"{self.name} says {say}")


FN2187 = Character("87", "Shooter")
print(FN2187.weapon)
Luke = Has_Script("Luke", "Blue Light Saber", 75, "Light")
print(Luke.weapon)
DV = Has_Script("Darth Vader", "Red Light Saber", 125, "Dark")
print(DV.weapon)
