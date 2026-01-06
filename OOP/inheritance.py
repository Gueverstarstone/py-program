# single inheritance
class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'
    

class Dog(Animal):
    bark = 'woof! woof! woof!!!'

jack = Dog('Jack')
print(jack.sound())
print(jack.bark)

# single inheritance
class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'
    

class Dog(Animal):
    bark = 'woof! woof! woof!!!'

    def sound(self):
        return f'{self.name} barks {self.bark}'

jack = Dog('Jack')
print(jack.sound())
print(jack.bark)

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

    # Call Animal.sound(), then append bark
    def sound(self):
        base = super().sound()
        return f'{base}, then {self.name} barks {self.bark}'

jack = Dog('Jack')
print(jack.sound())  # Jack makes a sound, then Jack barks woof! woof!! woof!!!

# multiple inheritance
# A simple way to demonstrate multiple inheritance is with a frog, which can both walk on land and swim in water:
class Walker:
    def walk(self):
        return 'I can walk on land'

class Swimmer:
    def swim(self):
        return 'I can swim in water'

# Amphibian inherits from both Walker and Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."

frog = Amphibian('Freddy')
print(frog.introduce())
# Output: I'm Freddy the frog. I can walk on land and I can swim in water.