# Define a Book class (blueprint for creating book objects)
class Book:
    def __init__(self, title, pages):
        # INSTANCE ATTRIBUTES (unique to each book object)
        self.title = title    # the book's title
        self.pages = pages    # the number of pages in the book

    def __len__(self):
        # MAGIC METHOD: called when you use len(book)
        # Returns the number of pages in the book
        return self.pages
    
    def __str__(self):
        # MAGIC METHOD: called when you use str(book) or print(book)
        # Returns a human-friendly string describing the book
        return f"'{self.title}' has {self.pages} pages"
    
    def __eq__(self, other):
        # MAGIC METHOD: called when you compare two books with ==
        # Returns True if both books have the same number of pages
        return self.pages == other.pages
    

# Create two Book objects (instances of the Book class)
book1 = Book('Built Wealth like a boss', 420)
book2 = Book('Be Your Own Start', 420)

# Call len() on each book (triggers __len__)
print(len(book1))   # Output: 420
print(len(book2))   # Output: 420

# Call str() on each book (triggers __str__)
print(str(book1))   # Output: 'Built Wealth like a boss' has 420 pages
print(str(book2))   # Output: 'Be Your Own Start' has 420 pages

# Compare the two books with == (triggers __eq__)
print(book1 == book2)   # Output: True (because both have 420 pages)


# Define a Cart class (blueprint for a shopping cart)
class Cart:
    def __init__(self):
        # INSTANCE ATTRIBUTE: each cart object has its own list of items
        self.items = []

    # INSTANCE METHOD: add an item to the cart
    def add(self, item):
        self.items.append(item)

    # INSTANCE METHOD: remove an item from the cart if it exists
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            # If item is not found, print a message
            print(f'{item} is not in cart')

    # INSTANCE METHOD: return the list of items in the cart
    def list_items(self):
        return self.items

    # MAGIC METHOD: defines behavior of len(cart)
    def __len__(self):
        return len(self.items)

    # MAGIC METHOD: defines behavior of cart[index]
    def __getitem__(self, index):
        return self.items[index]

    # MAGIC METHOD: defines behavior of 'item in cart'
    def __contains__(self, item):
        return item in self.items

    # MAGIC METHOD: defines behavior of iterating over the cart (for loops)
    def __iter__(self):
        return iter(self.items)


# Create a Cart object (an instance of the Cart class)
cart = Cart()

# Add items to the cart
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

# Iterate over the cart (triggers __iter__)
for item in cart:
    print(item, end=' ')  # Output: Laptop Wireless mouse Ergo keyboard Monitor

# Get the length of the cart (triggers __len__)
print(len(cart))  # Output: 4

# Access an item by index (triggers __getitem__)
print(cart[3])  # Output: Monitor

# Check if an item is in the cart (triggers __contains__)
print('Monitor' in cart)  # Output: True
print('banana' in cart)   # Output: False

# Remove an item from the cart
cart.remove('Ergo keyboard')

# List all items currently in the cart
print(cart.list_items())  # Output: ['Laptop', 'Wireless mouse', 'Monitor']

# Try to remove an item that doesn't exist
cart.remove('banana')  # Output: banana is not in cart




class Equal:
    def __init__(self,name,length):
        self.name = name
        self.length = length

    def __len__(self):
        return self.length
    
    def __str__(self):
        return self.name
