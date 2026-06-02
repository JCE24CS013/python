class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance! Withdrawal denied.")

    def get_balance(self):
        return f" Bankaccount (owner={self.owner},balance=(balamce={self.balance}"