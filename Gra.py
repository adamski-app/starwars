from My_files.Intro import music
from My_files.Sounds import sound
from My_files.End import end_music
import random
import time

class Weapon:
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def __str__(self):
        return "{}\nDescription: {}\nDamage: {}".format(self.name, self.description, self.damage)
class Blaster(Weapon):
    def __init__(self):
        super().__init__(name="Blaster",
                         description="Ranged weapon that fire bursts of particle beam energy called blaster bolts",
                         damage=150)
class Lightsaber(Weapon):
    def __init__(self):
        super().__init__(name="Lightsaber",
                         description="Lightsabers consist of a plasma blade, powered by a kyber crystal, that was emitted from a usually metal hilt",
                         damage=200)
class Person():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def __str__(self):
        return "{}".format(self.name, self.hp, self.damage)
class Storm_Commandos(Person):
    def __init__(self):
        super().__init__(name="Storm Commandos", hp=50, damage=5)
class Stormtrooper(Person):
    def __init__(self):
        super().__init__(name="Stormtrooper", hp=50, damage=5)
class Darth_Vader(Person):
    def __init__(self):
        super().__init__(name="Darth Vader", hp=200, damage=100)
class Player(Person):
    def __init__(self):
        super().__init__(name=None, hp=110, damage=50)

player = Player()
enemies = [Storm_Commandos, Stormtrooper]
wepones = [Lightsaber, Blaster]



def game():
    music()
    input("                             What is your name?\n                             ")
    with open("Intro.txt", encoding="utf-8") as plik:
        for i in plik:
           time.sleep(2), print(i)
    firs_location()


def firs_location():
    time.sleep(3)
    print("\nDo you want to search the room? \x1b[36m\nYes \ No\x1b[39m")
    decision = input().lower()

    if decision not in ("yes", "no"):
        print("Please enter a valid action")

    elif decision == "yes":
        time.sleep(1)
        print("You look around the room. Many unnecessary things around. Wait a minute, this picture hides a code box.")
        wylosowana_liczba = random.randint(1, 5)
        time.sleep(1)
        liczba_uzytkownika = int(input("        It must be some code, just guess one number. Damn, you have 5 tries.\n"))
        f = 5
        while f > 0:
            if liczba_uzytkownika == wylosowana_liczba:
                time.sleep(3)
                print("Yes good job! You unlock the lock ... What do we have inside ...? Damn it, it's a recording of Princess Leia! This must be delivered to the Rebels. ")
                exit_first_location()
                break
            elif liczba_uzytkownika < wylosowana_liczba:
                time.sleep(3)
                print("The number provided is too small, you have", f, " try. Try again!")
                liczba_uzytkownika = int(input("Try again: \n"))
                f = f - 1
            elif liczba_uzytkownika > wylosowana_liczba:
                time.sleep(3)
                print("The number provided is too big, you have", f, " try. Focus!")
                liczba_uzytkownika = int(input("Try again: \n"))
                f = f - 1
            if f == 0:
                zakoczenie()
    elif decision == "no":
        met_DV()

def exit_first_location():
    enemy_class = random.choice(enemies)
    enemy = enemy_class()
    wepones_class = random.choice(wepones)
    wepone = wepones_class()
    time.sleep(3)
    print(f"Oh shit! This is fuck'n {enemy}. We have big trublle!")
    time.sleep(3)
    print("All right, it's time to destroid your oponent, and back to home. ")
    time.sleep(3)


    while enemy.hp > 0 or player.hp > 0:
        print("Press A to attack")
        action = input().lower()
        if action == "a":
            enemy.hp = enemy.hp - player.damage
            time.sleep(2)
            print(f"You dealt {player.damage} damage to the {enemy}. He have {enemy.hp} health points!")
            player.hp = player.hp - enemy.damage
            time.sleep(2)
            print(f"{enemy} left you {player.hp} health points")

        if enemy.hp <= 0:
            time.sleep(3)
            print("Well done, you can go forward to Leias room!")
            break
    time.sleep(3)
    print(f"\nWait a second! {enemy} is drop something... WOW this is {wepone}\n")
    player.damage = player.damage + wepone.damage
    time.sleep(3)
    print(f"Your damage with {wepone.name} is {player.damage}")
    time.sleep(3)
    met_DV()

def zakoczenie():
    with open("End.txt", encoding="utf-8") as plik:
        for i in plik:
           time.sleep(2), print(i)
    time.sleep(2)
    end_music()


def met_DV():
    time.sleep(2)
    print(f"\nWhat are these sounds? Someone's breath ")
    sound()
    enemy = Darth_Vader()
    print(f"It's {enemy}!")
    time.sleep(2)

    while enemy.hp > 0 or player.hp > 0:
        print("Press A to attack")
        action = input().lower()
        if action == "a":
            enemy.hp = enemy.hp - player.damage
            player.hp = player.hp - enemy.damage
            time.sleep(2)
            print(f"You inflicted {player.damage} damage points {enemy}. He has {enemy.hp} health points left.")
            time.sleep(2)
            print(f"You have been dealt {enemy.damage} damage. You have {player.hp} health points left!")
        if player.hp <= 0:
            time.sleep(2)
            print("Darth Vader used his power. He threw you against the wall and pierced you with his lightsaber")
            break
        if enemy.hp <= 0:
            time.sleep(3)
            print("He is death")
        break

    zakoczenie()

game()




