from abc import ABC, abstractmethod   # Import Abstract Base Class tools

class Animal(ABC):   # Abstract Class
  @abstractmethod
  def make_sound(self):   # Abstract Method (must be implemented by child classes)
    pass

  def eat(self):   # Normal method (common to all animals)
    print("i am eating")
    
class Dog(Animal):   # Dog inherits from Animal
  def make_sound(self):   # Implementing abstract method
    print("Dog barking")
    
class Cat(Animal):   # Cat inherits from Animal
  def make_sound(self):   # Implementing abstract method
    print("Meow Meow")

class Snake(Animal):   # Snake inherits from Animal
  def make_sound(self):   # Implementing abstract method
    print("Hiss Hiss")    

# Object creation and method calling
d1 = Dog()        
d1.eat()  # Inherited from Animal → Output: i am eating
d1.make_sound()  # Dog's implementation → Output: Dog barking

c1 = Cat()
c1.make_sound()  # Cat's implementation → Output: Meow Meow

s1 = Snake()
s1.make_sound() # Snake's implementation → Output: Hiss Hiss
