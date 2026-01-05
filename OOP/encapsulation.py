# Example 1: Wallet with a "protected" attribute (_balance)
class Wallet:
    def __init__(self, balance):
        # Single underscore means "protected" by convention (not enforced)
        self._balance = balance

    def deposit(self, amount):
        # Only allow positive deposits
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        # Only allow withdrawals if amount is positive and less than balance
        if 0 < amount <= self._balance:
            self._balance -= amount


# Example 2: Wallet with a "private" attribute (__balance)
class Wallet:
    def __init__(self, balance):
        # Double underscore triggers name mangling (harder to access directly)
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

account = Wallet(500)
# print(account.__balance)  # ERROR: can't access private attribute directly


# Example 3: Wallet with a getter method for encapsulation
class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        # Public method to safely access private balance
        return self.__balance
    

# Demonstration of usage
acct_one = Wallet(100)
acct_one.deposit(50)
print(acct_one.get_balance())   # Output: 150

acct_two = Wallet(230)
acct_two.deposit(100)
print(acct_two.get_balance())   # Output: 330

acct_two = Wallet(230)
acct_two.withdraw(100)
print(acct_two.get_balance())   # Output: 130

acct_two.deposit(500)
print(acct_two.get_balance())   # Output: 630


# Example 4: Wallet with private validation method
class Wallet:
   def __init__(self):
       # Start with zero balance
       self.__balance = 0

   def __validate(self, amount):
       # Private helper method to check if amount is valid
       if amount < 0:
           raise ValueError('Amount must be positive')

   def deposit(self, amount):
       # Validate before deposit
       self.__validate(amount)
       self.__balance += amount

   def withdraw(self, amount):
       # Validate before withdrawal
       self.__validate(amount)
       if amount > self.__balance:
           raise ValueError('Insufficient funds')
       self.__balance -= amount

   def get_balance(self):
       # Public method to check balance safely
       return self.__balance


# Demonstration of usage with error handling
acct_one = Wallet()
acct_one.deposit(4)  # This will raise ValueError because amount must be positive
print(acct_one.get_balance())   # Output: 0 (deposit failed)

acct_one.deposit(50)
print(acct_one.get_balance())   # Output: 50

acct_one.withdraw(-8)  # Raises ValueError: Amount must be positive
acct_one.withdraw(58)  # Raises ValueError: Insufficient funds