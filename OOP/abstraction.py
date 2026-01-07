from abc import ABC, abstractmethod

# -------------------------------
# Example 1: Abstract Animal Class
# -------------------------------

# Animal is an abstract base class (cannot be instantiated directly)
class Animal(ABC):  # Inherits from ABC (Abstract Base Class)
   @abstractmethod  # Marks this method as abstract (must be overridden in subclasses)
   def make_sound(self):  # Defines the interface, but no implementation
       pass

# Concrete subclass that provides its own implementation of make_sound()
class Dog(Animal):
   def make_sound(self):
       print('Woof!')

# Another concrete subclass
class Cat(Animal):
   def make_sound(self):
       print('Meow!')

# Another concrete subclass
class Monkey(Animal):
   def make_sound(self):
       print('Ooh ooh aah aah!')

# Create instances of each concrete class
animals = [Dog(), Cat(), Monkey()]

# Loop through the instances and call their make_sound() methods
for animal in animals:
   animal.make_sound()

# Output:
# Woof!
# Meow!
# Ooh ooh aah aah!


# -------------------------------
# Example 2: Abstract TalkingToy Class
# -------------------------------

from abc import ABC, abstractmethod

# Abstract base class that defines a blueprint for any toy that can "speak"
class TalkingToy(ABC):
   def __init__(self, name):
       self.name = name

   @abstractmethod  # Subclasses must implement this method
   def speak(self):
       pass

# Concrete subclass: RobotToy
class RobotToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says beep boop! I am a robot!')

# Concrete subclass: TeddyBearToy
class TeddyBearToy(TalkingToy):
   def speak(self):
       print(f"{self.name} says hug me! I'm cuddly!")

# Concrete subclass: DinosaurToy
class DinosaurToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says ROOOOAR!')

# Create toy instances
rusty = RobotToy('Rusty')
fluffy = TeddyBearToy('Fluffy')
rex = DinosaurToy('Rex')

# Store them in a list
toys = [rusty, fluffy, rex]

# Loop through toys and call their speak() methods
for toy in toys:
   toy.speak()

# Output:
# Rusty says beep boop! I am a robot!
# Fluffy says hug me! I'm cuddly!
# Rex says ROOOOAR!
