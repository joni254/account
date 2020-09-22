#python code that depicts a bank account functions 
# no global variables for now

class Account:
    #initial function
    def __init__(self,Name,Balance):
        self.Name = Name
        self.Balance = Balance
    #deposit function
    def Credit(self, Deposit):
        self.Balance = self.Balance + Deposit

    # Withdraw function
    def Debit(self, Withdraw):
        self.Balance = self.Balance - Withdraw

    #Access Account Balance
    def get_balance(self):
        return self.Balance
    
    # Access account holder name
    def get_name(self):
        return self.Name

    # Change Holder name
    def set_name(self, Name):
        self.Name = Name

#create an instance of the class

i = Account('john', 0)
print(i.get_name(), 'has an account balance of', i.get_balance() )
    

    