# Object Oriented Programming Challenge
#
# For this challenge, create a bank account class that has two attributes:
#
# owner
# balance
#
# and two methods:
#
# deposit
# withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
#
# class Account:
#     pass
#
# 1. Instantiate the class
# acct1 = Account('Sid',100)

# 2. Print the object
# print(acct1)

# Account owner:   Sid
# Account balance: $100

# 3. Show the account owner attribute
# acct1.owner

# 'Sid'

# 4. Show the account balance attribute
# acct1.balance

# 100

# 5. Make a series of deposits and withdrawals
# acct1.deposit(50)

# Deposit Accepted

# acct1.withdraw(75)

# Withdrawal Accepted

# 6. Make a withdrawal that exceeds the available balance
# acct1.withdraw(500)

# Funds Unavailable!

# ========================================================================

print("\n================================================================================================\n")


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"Account Owner : {self.owner}")
        print(f"Account Balance : {self.balance}")

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("Deposit Accepted")
        print(f"Total Balance : {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount >= self.balance:
            print(f"Withdrawing Amount : {self.amount}")
            print("Withdrawal Rejected!!!")
            print("Funds Unavailable")
            print(f"Total Balance : {self.balance}")
        else:
            self.balance -= self.amount
            print(f"Withdrawing Amount : {self.amount}")
            print("Withdrawal Accepted!!!")
            print(f"Total Balance : {self.balance}")


# Instantiate the class
acct1 = Account("Sid", 100)

print("Account Owner : ")
print(acct1.owner)

print("Account Balance : ")
print(acct1.balance)

print("Adding 50 to Balance")
acct1.deposit(50)

print("Withdrawing Amount from Balance")
acct1.withdraw(70)
print("Withdrawing Amount from Balance")
acct1.withdraw(200)
