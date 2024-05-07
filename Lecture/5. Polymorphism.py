# Polymorphism is the ability of an object to take on multiple forms.
class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self):
        print(f"{self.name} says stop or I'll shoot")


class Has_Script(Character):
    def __init__(self, name, weapon, mc, side):
        super().__init__(name, weapon)
        self.mc = mc
        self.side = side

    def speak(self, say):
        print(f"{self.name} says {say}")

    def speak(self, other, say):
        print(f"{self.name} says {other.name} {say}")


FN2187 = Character("87", "Shooter")
Luke = Has_Script("Luke", "Light Saber", 75, "Light")
DV = Has_Script("Darth Vader", "Light Saber", 125, "Dark")

FN2187.speak()
# DV.speak()
DV.speak(FN2187, "I am your father")
# Luke.speak("Noooooo")
