class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the BankAccount with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the amount from the account balance if sufficient funds exist.
        Return True if the withdrawal was successful, otherwise return False."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.account_balance:
            return False  # Insufficient funds
        self.account_balance -= amount
        return True

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
