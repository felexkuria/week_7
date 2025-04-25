# Code Along Challenge ✨:
# Create a Puppy class with a breed attribute set to "Golden Retriever". Then, make a my_puppy object and print its breed!
class Puppy:
    breed="Golden Retriever"
    def bark (self):
        print("Woof! Woof!")

my_puppy=Puppy()
print(my_puppy.breed)
my_puppy.bark()

# 👩💻 SECTION 5: Hands-On Lab (15 mins)
# Build a Book Class!

# Define the class with title and author attributes.
# Add a method display_info() that prints:
# "[Title] by [Author] 📖".
# Create an object and test it!
class Book:
    title="Richest Man In bablyon "
    author="Samil Isamil"
    def display_info(self):
        print(f"{self.title} by {self.author}")

my_book=Book()
my_book.display_info()
# 💪 Tina’s Reinforcement Challenge

# Create a BankAccount class with balance (starts at 0).
# Add a deposit(amount) method that adds to the balance.\
#Add a withdraw method that subtracts from the balance.
# Make a check_balance() method to print the current balance.
# Create an object and test it!\
class BankAccount:
    balance=0
    amount=int(input("Enter You Bank Balance "))
    total_balance=balance+amount
    def depoist(self):
        print(f"Your Total Bank Balance is {self.total_balance}")
    def check_balance(self ):
        print(f" Your Bank Balance is {self.total_balance}")
felex_account=BankAccount()
# felex_account.check_balance()

