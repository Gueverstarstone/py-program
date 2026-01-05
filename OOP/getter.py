import math

class Circle:
    def __init__(self, radius):
        # Initialize the circle with a radius
        self._radius = radius

    @property
    def radius(self):
        # Getter for radius (acts like an attribute, not a method)
        return self._radius
    
    @property
    def area(self):
        # Getter for area (calculated dynamically from radius)
        # Rounded to 2 decimal places
        return round(math.pi * (self._radius ** 2), 2)
    
# Create a Circle object with radius 3
my_circle = Circle(3)

# Access radius using the property (no parentheses needed)
print(my_circle.radius)   # Output: 3

# Access area using the property (calculated automatically)
print(my_circle.area)     # Output: 28.27

# 👉 Without @property, you’d have to write c.area() like a method.
# But since we used @property, it feels like a normal attribute.
# print(my_circle.area())  # ❌ This would cause an error, because area is not a method anymore.
