# -------------------------------
# Example 1: Polymorphism with Animals
# -------------------------------

class Cat:
   def speak(self):
       return "A cat meow"

class Bird:
   def speak(self):
       return "A bird tweet"
  
class Monkey:
   def speak(self):
       return "A monkey ooh ooh aah aah ooh ooh aah aah"

# Function that works with any object that has a .speak() method
def animal_sound(animal):
   print(animal.speak())

# Polymorphic calls: same function, different outputs depending on the object
animal_sound(Cat())     # Output: A cat meow
animal_sound(Bird())    # Output: A bird tweet
animal_sound(Monkey())  # Output: A monkey ooh ooh aah aah ooh ooh aah aah


# -------------------------------
# Example 2: Polymorphism with Social Media
# -------------------------------

class Twitter:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"🐦 Tweet: '{self.content}' (280 chars max)"

class Instagram:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"📸 Instagram Post: '{self.content}' + ✨ filters"

class LinkedIn:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"

# Function that works with any object that has a .post() method
def start(social_media):
   print(social_media.post())

# Instances of different social media platforms
tweet = Twitter('Just learned Python polymorphism!')
photo = Instagram('Sunset vibes 🌅')
article = LinkedIn('Why OOP matters in 2024')

# Polymorphic calls: same function, different outputs depending on the object
start(tweet)   # 🐦 Tweet: 'Just learned Python polymorphism!' (280 chars max)
start(photo)   # 📸 Instagram Post: 'Sunset vibes 🌅' + ✨ filters
start(article) # 💼 LinkedIn Article: 'Why OOP matters in 2024' (Professional Mode)


# -------------------------------
# Example 3: Inheritance + Polymorphism
# -------------------------------

class Animal:
   def speak(self):
       return 'Some generic sound'

# Subclasses override the speak() method
class Cat(Animal):
   def speak(self):
       return 'A cat meow'

class Dog(Animal):
   def speak(self):
       return 'A dog barks woof woof'

class Monkey(Animal):
   def speak(self):
       return 'A monkey ooh ooh aah aah ooh ooh aah aah'
  
# Each subclass provides its own version of speak()
print(Cat().speak())     # A cat meow
print(Dog().speak())     # A dog barks woof woof
print(Monkey().speak())  # A monkey ooh ooh aah aah ooh ooh aah aah
print(Animal().speak())  # Some generic sound


# -------------------------------
# Example 4: Name Mangling
# -------------------------------

class Example:
    def __init__(self, internal, private):
        # Single underscore = "internal use" (convention, but still accessible)
        self._internal = internal
        # Double underscore = triggers name mangling (_Example__private internally)
        self.__private = private

# Create an instance with two attributes
example1 = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)

# __dict__ shows all instance attributes in a dictionary form
print(example1.__dict__)
# Output:
# {
#   '_internal': 'I can be accessed from outside the class, but should not',
#   '_Example__private': 'I cannot be accessed directly from outside the class'
# }
