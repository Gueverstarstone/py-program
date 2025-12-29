# Example 1: Using setattr, getattr, hasattr, delattr
class Dog:
    def __init__(self, name):
        self.name = name

rex = Dog("Rex")

# Dynamically add a new attribute "age" to the object
setattr(rex, "age", 5)

# Access the dynamically added attribute
print(getattr(rex, "age"))      # Output: 5

# Check if the attribute exists
print(hasattr(rex, "age"))      # Output: True

# Remove the attribute dynamically
delattr(rex, "age")

# Check again if the attribute exists
print(hasattr(rex, "age"))      # Output: False


# Example 2: Using getattr with default values
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Wantam', 25)

# Direct access
print(person.name)              # Output: Wantam

# Dynamic access using getattr
print(getattr(person, 'name'))  # Output: Wantam
print(getattr(person, 'age'))   # Output: 25

# Try to access a missing attribute, provide default fallback
print(getattr(person, 'city', 'ronga'))  # Output: ronga


# Example 3: User input with getattr
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30)

# Ask user which attribute they want to see
attr_name = input('Enter the attribute you want to see: ')
# Dynamically fetch it, or show "Attribute not found" if missing
print(getattr(person, attr_name, 'Attribute not found'))


# Example 4: Listing attributes with dir()
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30)

# Loop through all attributes of the object
for attr in dir(person):
    # Skip dunder methods (__init__, __str__) and methods (callables)
    if not attr.startswith('__') and not callable(getattr(person, attr)): 
        value = getattr(person, attr)
        print(f'{attr}: {value}')
# Output: name: John Doe, age: 30


# Example 5: Setting attributes from a dictionary
class Configuration:
    pass

# Simulated runtime settings
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Dynamically attach each key/value as an attribute
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

# Access dynamically created attributes
print(config_obj.server_url)   # Output: https://api.example.com
print(config_obj.timeout_sec)  # Output: 30


# Example 6: Validating attributes with hasattr
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)

required_attributes = ['name', 'price', 'inventory_id']

# Check if all required attributes exist
for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        print(f'{attr}: {getattr(product_a, attr)}')
# Output: name: T-Shirt, price: 25, ERROR for inventory_id


# Example 7: Removing attributes dynamically with delattr
class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token   # sensitive
        self.temp_counter = 0     # temporary

session = UserSession(101, 'a1b2c3d4e5')

# Attributes to clean before saving
attributes_to_clean = ['auth_token', 'temp_counter']

# Remove them dynamically
for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')

# Show remaining attributes
for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f' - {attr}: {getattr(session, attr)}')
# Output: only user_id remains
