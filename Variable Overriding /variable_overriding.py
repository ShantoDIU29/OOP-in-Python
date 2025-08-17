class Animal:
    def __init__(self, name):
        self.name = name          # Set the 'name' attribute for this object
        self.color = "white"      # Set default 'color' attribute as "white"
    def eat(self):
        print(self.color, self.name, "is eating")  # Print color and name when eating
        
class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)     # Call Animal's constructor to set 'name' and default 'color'
        self.color = color         # Override 'color' with the new value passed for Dog
    def bark(self):
        print(self.color, self.name, "is barking")  # Print color and name when barking
        
d1 = Dog("Rover", "Brown")      # Create a Dog object with name="Rover" and color="Brown"
d1.bark()                       # Calls Dog's bark() → prints: "Brown Rover is barking"
d1.eat()                        # Calls Animal's eat() → prints: "Brown Rover is eating"
