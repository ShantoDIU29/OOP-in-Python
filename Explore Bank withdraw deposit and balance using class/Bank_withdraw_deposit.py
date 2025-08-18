class Bank:
    def __init__(self, balance):
        self.balance = balance     # Initial balance when the account is created
        self.min_withdraw = 100    # Minimum amount allowed to withdraw
        self.max_withdraw = 10000  # Maximum amount allowed to withdraw
    
    def get_balance(self):
        return self.balance        # Return the current balance
   
    def deposit(self, amount):
        if amount > 0:             # Deposit only positive amounts
            self.balance += amount
      
    def withdrew(self, amount):
        if amount < self.min_withdraw:   # Case 1: amount too small
            print(f'You cannot withdraw below: {self.min_withdraw}') 
        elif amount > self.max_withdraw: # Case 2: amount too large
            print(f'You cannot withdraw more than: {self.max_withdraw}')
        else:                            # Case 3: valid withdrawal
            self.balance -= amount
            print(f'Here is your money: {amount}')    


# Create a Bank account with 150000 balance
brac = Bank(150000)
brac.withdrew(25)       # Too small (below min_withdraw)
brac.withdrew(6000000)  # Too big (above max_withdraw)
brac.withdrew(1000)     # Valid withdrawal (balance will decrease by 1000)


# Another account with 6000 balance
dbbl = Bank(6000)
dbbl.deposit(2000)      # Deposit 2000
dbbl.deposit(2000)      # Deposit another 2000
print(dbbl.get_balance())  # Final balance: 6000 + 2000 + 2000 = 10000
