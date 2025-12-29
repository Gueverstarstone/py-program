# Define a Computer class
class Computer:
    # CLASS-LEVEL ATTRIBUTE (shared by all objects of this class)
    shape = 'square'

    def __init__(self, name, year):
        # INSTANCE ATTRIBUTES (unique to each object)
        self.name = name      # belongs to the specific object
        self.year = year      # belongs to the specific object

    # CLASS METHOD (actually an instance method here, but belongs to the class definition)
    def config(self):
        # Uses instance attributes to print details
        print(f'My computer is {self.name.upper()} which was manufactured in {self.year}')


# Create two Computer objects (instances) with different data
com3 = Computer('dell', 2005)
com4 = Computer('hp', 2012)

# Call the config method (INSTANCE METHOD) on each object
com3.config()   # Output: My computer is DELL which was manufactured in 2005
com4.config()   # Output: My computer is HP which was manufactured in 2012

# Access INSTANCE ATTRIBUTE directly
print(com3.name)   # Output: dell

# Access CLASS-LEVEL ATTRIBUTE directly from the class
print(Computer.shape)   # Output: square

# # ⚠️ This will cause an error because 'name' is not a CLASS attribute
# # It's only defined per object (instance attribute)
# print(Computer.name)    # AttributeError


# Define another Computer class (this overwrites the previous one)
class Computer:

    def __init__(self):
        # No instance attributes initialized here
        pass

    # INSTANCE METHOD (belongs to the class, but acts on objects)
    def config(self):
        # Prints fixed configuration details (doesn't use instance attributes)
        print('i5, 16GB, 1TB')


# Create two Computer objects using the new class
com1 = Computer()
com2 = Computer()

# Print the type of com1 (shows it's a Computer object)
print(type(com1))   # Output: <class '__main__.Computer'>

# Call the config method using the class directly and passing the object
Computer.config(com1)   # Output: i5, 16GB, 1TB
Computer.config(com2)   # Output: i5, 16GB, 1TB

# Call the config method using the object itself
com1.config()   # Output: i5, 16GB, 1TB
com2.config()   # Output: i5, 16GB, 1TB


# Define a Dog class
class Dog:
    def __init__(self, name):
        # INSTANCE ATTRIBUTE (unique to each dog)
        self.name = name

    # INSTANCE METHOD (belongs to the class, acts on each object)
    def bark(self):
        # Uses the instance attribute 'name'
        print(f'{self.name} says woof!')


# Create a Dog object
dog1 = Dog('rex')

# Call the bark method (INSTANCE METHOD)
dog1.bark()   # Output: rex says woof!

# Access INSTANCE ATTRIBUTE directly
print(dog1.name)   # Output: rex
