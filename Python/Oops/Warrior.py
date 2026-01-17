from abc import ABC, abstractclassmethod
import random


class Character(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractclassmethod
    def attack(self):
        pass
    
class Warrior(Character):
    def attack(self):
        attack = random.randint(10,100)
        print(f"warrior {self.name} has attacked with sword swing of {attack} damage")
    
class Mage(Character):
    def attack(self):
        attack = random.randint(10,200)
        if random.random()<0.2:
            print(f"mage {self.name} has attacked with fireball of {attack} damage")
        else:
            print(f"Mage {self.name} has missed the attack")
            
heros = [Warrior("Himanshu",100),Mage("Nikhil",80)]

for i in heros:
    i.attack()
    