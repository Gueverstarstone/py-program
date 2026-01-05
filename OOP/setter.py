class Circle:
    def __init__(self, radius):
        # Initialize the circle with a radius
        # Using a "protected" attribute (_radius) by convention
        self._radius = radius

    @property
    def radius(self):
        # Getter method: allows you to access _radius like an attribute
        # Example: print(my_circle.radius) will call this method
        return self._radius
    
    @radius.setter
    def radius(self, value):
        # Setter method: controls how _radius can be modified
        # Validation: radius must always be positive
        if value <= 0:
            raise ValueError('Radius must be positive')
        # If validation passes, update the radius
        self._radius = value

# Create a Circle object with radius 3
my_circle = Circle(3)

# Access the radius using the property (calls the getter)
print('Initial radius:', my_circle.radius)   # Output: Initial radius: 3

# Modify the radius using the setter
# Since 8 > 0, this passes validation and updates _radius
my_circle.radius = 8

# Access the updated radius using the getter
print('After modifying the radius:', my_circle.radius)  # Output: After modifying the radius: 8

# Getter vs Setter in the Analogy
# Getter (@property or get_value)

# Think of the glass window on the vending machine.

# It lets you see what’s inside (read‑only access).

# You can check the current state (e.g., how much balance you have, what snacks are available).

# But it doesn’t change anything — it only reveals information.

# Setter (@attr.setter)

# Think of the coin slot.

# It’s where you insert coins (write/update access).

# The machine validates the coin before accepting it.

# This is where rules are enforced (e.g., “only positive amounts,” “only valid currency”).