# Define a dictionary with product names as keys and prices as values
products = {
    'benz': 2000,
    'subaru': 700,
    'BMW': 4000,
    'honda': 1000
}

# Loop through dictionary items (key-value pairs) as tuples
for price in products.items():
    print(price)   # prints ('benz', 2000), ('subaru', 700), etc.

# Loop through dictionary directly (iterates over keys only)
for product in products:
    print(product)   # prints benz, subaru, BMW, honda

# Loop through dictionary items, unpacking into key and value
for product, price in products.items():
    print(product, price)   # prints benz 2000, subaru 700, etc.

# Apply a 20% discount to each product price and update dictionary
for product, price in products.items():
    products[product] = round(price * 0.8)
print(products)   # prints updated dictionary with discounted prices

# Enumerate over dictionary keys (returns index, key)
for product in enumerate(products):
    print(product)   # prints (0, 'benz'), (1, 'subaru'), etc.

# Enumerate over dictionary keys with unpacking
for index, product in enumerate(products):
    print(index, product)   # prints index and key separately

# Enumerate over dictionary values
for index, product in enumerate(products.values()):
    print(index, product)   # prints index and value separately

# Enumerate over dictionary items (key-value pairs)
for index, product in enumerate(products.items()):
    print(index, product)   # prints index and tuple (key, value)

# Enumerate over dictionary items starting index at 1
for index, product in enumerate(products.items(), 1):
    print(index, product)   # prints index starting from 1 and tuple (key, value)
