# -------------------------------
# Example 1: Single Inheritance
# -------------------------------

# Base class (parent)
class Animal:
    def __init__(self, name):
        # Every animal has a name
        self.name = name

    def sound(self):
        # Default sound method for any animal
        return f'{self.name} makes a sound'
    

# Child class (Dog) inherits from Animal
class Dog(Animal):
    # Class attribute specific to Dog
    bark = 'woof! woof! woof!!!'

# Create a Dog object named Jack
jack = Dog('Jack')
print(jack.sound())  # Inherits Animal.sound()
print(jack.bark)     # Access Dog-specific attribute


# -------------------------------
# Example 2: Method Overriding
# -------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'
    

class Dog(Animal):
    bark = 'woof! woof! woof!!!'

    # Override the sound() method from Animal
    def sound(self):
        return f'{self.name} barks {self.bark}'

jack = Dog('Jack')
print(jack.sound())  # Uses Dog's overridden sound()
print(jack.bark)


# -------------------------------
# Example 3: Using super()
# -------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

    # Extend Animal.sound() using super()
    def sound(self):
        # Call the parent class method first
        base = super().sound()
        # Then add Dog-specific behavior
        return f'{base}, then {self.name} barks {self.bark}'

jack = Dog('Jack')
print(jack.sound())  
# Output: Jack makes a sound, then Jack barks woof! woof!! woof!!!


# -------------------------------
# Example 4: Multiple Inheritance
# -------------------------------

# First parent class
class Walker:
    def walk(self):
        return 'I can walk on land'

# Second parent class
class Swimmer:
    def swim(self):
        return 'I can swim in water'

# Amphibian inherits from both Walker and Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        # Can use methods from both parent classes
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."

frog = Amphibian('Freddy')
print(frog.introduce())
# Output: I'm Freddy the frog. I can walk on land and I can swim in water.
