class Animal:

    def __init__(self, name, num_legs, has_tail, color, species):
        self.name = name
        self.num_legs = num_legs
        self.has_tail = has_tail
        self.color = color
        self.species = species

    def say_name(self):
        print(f"my name is {self.name}!")


duck1 = Animal("Greg", 2, False, "White", "Duck")
bear1 = Animal("Karl", 4, False, "Brown", "Bear")

duck1.say_name()
bear1.say_name()
