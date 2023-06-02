class Char:

    def __init__(self, name, job, race, health, hairColor):
        self.name = name
        self.job = job
        self.race = race
        self.health = health
        self.hairColor = hairColor

    def info(self):
        print(f"Name: {self.name}")
        print(f"Job: {self.job}")
        print(f"Race: {self.race}")
        print(f"Health: {self.health}")
        print(f"Hair Color: {self.hairColor}")

char1 = Char("Derek", "Barbarian", "Elf", 200, "Blue")
char2 = Char("Pam", "Wizard", "Ork", 150, "Brown")
char3 = Char("Alex", "Monk", "Dwarf", 275, "Red")

char1.info()
