#Class BankAccount :
def __init__(self, account_number, balance=0):
    self.account_number = account_number
    self.balance = balance
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposited {amount}.new balance is {self.balance}")
        else:
            print("invalid amount. deposit failed.")
            def withdraw(self, amount):
                if amount > 0 and amount <= self.balance:
                    self.balance -= amount 
                    print(f"withdrew {amount}.new balance is {self.balanced}")
                else:
                    print("invalid amount . withdrawal failed.")
                    def get_balance(self):
                        return self.balance
                    
        
