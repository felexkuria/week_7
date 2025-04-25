class Employee:
    def __init__(self,name,id,workStation):
        self.name=name
        self.id=id
        self.workStation=workStation

felex=Employee("Felex",1,"Mombasa")
print(felex.name)

class Mpesa:
    def __init__(self):
        self.balance=0
        intial_amount=int(input("Enter Intial Amount To Be Deposited "))
        self.balance+=intial_amount
        print(f"Your Initial Balance is {self.balance}")

    def depoist(self):
        self.amount=int(input("Enter Amount To Be Deposited "))
        self.balance+=self.amount
        print(f"Your Current Balance is {self.balance}")
       
    # def withdraw(self, amount):
    #     self.amount=amount
      
    #     amount=amount-self.balance
    # def check_balance(self):
    #     print(f"Your Current Balance is {self.balance}")

felex=Mpesa()
felex.depoist()

# emma =Mpesa()
# emma.check_balance()
# emma.depoist(500)
# emma.check_balance()
# emma.withdraw(200)

