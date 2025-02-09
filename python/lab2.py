from dataclasses import dataclass

@dataclass
class Animal:
    legs: int
    
    def talk(self):
        print("random sound")
    
    def leg_count(self):
        print(f"I have {self.legs} legs.")

@dataclass
class Mammal(Animal):
    lungs: int

    def breath(self):
        print("breathing")

class Dog(Mammal):
    def __init__(self):
        self.legs = 4
        self.lungs = 2
        
    def breath(self):
        print("breathing with tounge out")
        
    def talk(self):
        print("Bark!")
    
@dataclass
class Human(Mammal):
    def __init__(self):
        self.legs = 2
        self.lungs = 2
        self.arms = 2
        
    def talk(self):
        print("Hey there!")
        
        
animal = Animal(3)
mammal = Mammal(4,2)
dog = Dog()
human = Human()

animal.talk()
animal.leg_count()
mammal.talk()
mammal.leg_count()
mammal.breath()
dog.talk()
dog.leg_count()
dog.breath()
human.talk()
human.leg_count()
human.breath()