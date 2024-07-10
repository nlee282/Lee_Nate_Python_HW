class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Invalid amount")
            return False

    def withdraw(self, amount):
        if amount>0:
            if amount<=self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("Insufficient Funds.")
                return False
        else:
            return False
        
    
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def add_interest(self, interestRate):
        self.balance = self.balance * interestRate
        return self.balance

bankAccount1 = BankAccount(1234, 100)
savingsAccount1 = SavingsAccount(5678, 100)
print(bankAccount1.get_balance()==100)
print(bankAccount1.withdraw(101)==False)
print(bankAccount1.deposit(100)==200)
print(bankAccount1.withdraw(2000)==False)
print(savingsAccount1.add_interest(10)==1000)
