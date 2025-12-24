# Define a dictionary named car with keys: name, year, country, and type (list of models)
car ={
    'name': 'subaru',
    'year': 2005,
    'country': 'kenya',
    'type': ['sti','forester','sg5']
}

# Access the value of the 'type' key (prints the list of models)
print(car['type'])

# Update the value of the 'year' key from 2005 to 2006
car['year'] = 2006
print(car)   # prints the updated dictionary


# --- Using the dict() constructor ---
# Create a dictionary by passing a list of tuples (key, value) pairs
vehicle = dict([('name', 'subaru',),('year', 2005),('country', 'kenya'),('type', ['sti','forester','sg5'])])

# Access the value of the 'country' key
print(vehicle['country'])

# Update the 'country' key from 'kenya' to 'Japan'
vehicle['country'] = 'Japan'
print(vehicle)   # prints updated dictionary

# Print all values in the dictionary
print(vehicle.values())


# --- Another dictionary example ---
car ={
    'name': 'subaru',
    'year': 2005,
    'country': 'kenya',
    'type': ['sti','forester','sg5']
}

# Print the list stored under 'type'
print(car['type'])

# Update the 'year' key to 2006
car['year'] = 2006
print(car)

# Use .get() to safely access a key that doesn’t exist.
# If 'manufacturer' is missing, return the default value 'Germany'
print(car.get('manufacturer','Germany'))

# Print all keys in the dictionary
print(car.keys())

# Print all values in the dictionary
print(car.values())

# Print all key-value pairs as tuples
print(car.items())

# Remove the key 'name' and return its value
car.pop('name')
print(car)

# Remove and return the last inserted key-value pair
car.popitem()
