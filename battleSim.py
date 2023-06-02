import random

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def info(self):
        print(f"{self.name}:")
        print(self.health)

    def attack(self, target):
        print(f"{self.name} attacks!")
        damage = random.randint(0, 20)
        if damage < 3:
            print(f"{self.name} missed!")
        elif damage >= 3 and damage < 20:
            print(f"{self.name} hit! Minus {damage*2} health!")
            target.health -= damage
        elif damage == 20:
            print(f"{self.name} landed a critical hit! Minus {damage} health!")
            target.health -= damage * 2

    def special(self, target):
        print(f"{self.name} attempts to perform a special attack!")
        hit = random.randint(0,6)
        if hit < 6:
            print(f"{self.name}'s special attack failed!")
        elif hit == 6:
            print(f"{self.name}'s special attack succeeded!")
            if self.name == "Ebeneezer Scrooge":
                print(f"{target.name} is hit with a bag o' gold!")
                target.health -= 60
            elif self.name == "Jack Black":
                print(f"{target.name} is hit with the righteous sound of rock!")
                target.health -= 60

    def potion(self):
        print(f"{self.name} drinks a potion")
        print(f"{self.name}'s health has increased by 10")
        self.health += 10

    def choose_action(self, choice, target,):
        if choice == "A" or choice == "Attack":
            self.attack(target)
        if choice == "D" or choice == "Drink Potion":
            self.potion()
        if choice == "I" or choice == "Info":
            self.info()
        if choice == "S" or choice == "Special attack":
            self.special(target)

player1 = Player("Ebeneezer Scrooge", 100)
player2 = Player("Jack Black", 420)

# game loop
while player1.health > 0 and player2.health > 0:
    print("What would you like to do?")
    print("(A)ttack (D)rink Potion, attempt a (S)pecial attack or find out (I)nfo?")

    choice = input("> ")
    player1.choose_action(choice, player2)

    if choice == "info" or choice == "I":
        choice = "I"
    elif player2.health > 300:
        choice = "A"
    elif player2.health < 50:
        choice = "D"
    else:
        choice = random.choice(["A", "D", "S"])

    player2.choose_action(choice, player1)
