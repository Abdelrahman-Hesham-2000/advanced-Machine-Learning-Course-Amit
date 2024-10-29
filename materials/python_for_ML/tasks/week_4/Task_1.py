class Bank_Account:
    def __init__(self,balance):
        self.balance=balance
            
    def deposit(self,amount):
        if amount<0:
            print("please enter positive number")
        else:        
           self.balance += amount
           print(f'Deposited {amount}. New balance: {self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient funds')
        elif amount<0:
            print("please enter positive number")    
        else:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')

    def check_balance(self):
        print(f'Current balance: {self.balance}')


if __name__=="__main__":
    output=Bank_Account(100)
    output.deposit(50)
    output.withdraw(30)