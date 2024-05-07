# A class is a blueprint or template that defines the properties and behavior of an object. An Object is an instances of a class, created using the class definition.
class Character:
    def __init__(self, name, weapon, mc):
        self.name = name
        self.weapon = weapon
        self.mc = mc

    def speak(self, say):
        print(f"{self.name} says {say}")


Luke = Character("Luke", "Light Saber", 75)
DV = Character("Darth Vader", "Light Saber", 125)

DV.speak("I am your father")
Luke.speak("Noooooooo")
