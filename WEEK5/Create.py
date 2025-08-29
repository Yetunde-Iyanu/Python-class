# 1. Creating s class structure 
class Superhero:
    def __init__(self, name, power):
        # attributes (characteristics)
        self.name = name
        self.power = power
    
    def use_power(self):
        # method (action)
        return f"{self.name} uses {self.power}!"

# Child class (inherits from Superhero)
class FlyingHero(Superhero):
    def __init__(self, name, power, speed):
        # inherit name and power from parent
        super().__init__(name, power)
        self.speed = speed
    
    # method overriding (polymorphism)
    def use_power(self):
        return f"{self.name} flies at {self.speed} km/h using {self.power}!"

hero1 = Superhero("Spiderman", "Web Shooting")
print(hero1.use_power())   

hero2 = FlyingHero("Superman", "Super Strength", 500)
print(hero2.use_power())  

# 2. Create a program that includes animals or vehicles with the same action
# Parent class
class Vehicle:
    def move(self):
        # generic action
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving")


class Plane(Vehicle):
    def move(self):
        print("Flying ")


class Boat(Vehicle):
    def move(self):
        print("Sailing")


v1 = Car()
v2 = Plane()
v3 = Boat()

# Polymorphism in action (same method name, different behavior)
v1.move()  
v2.move()  
v3.move()  


