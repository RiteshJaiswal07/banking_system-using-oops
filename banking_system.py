"""parent class : user
   holds  detail about an user
   has a function to show user details
   child class : bank
   stores details about the bank details
   stores details about the  amount
   allows for deposit ,view balance, withdraw"""

#parent class
class user:
    def __init__(self, name, age,  gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("personal  details")
        print(f"""
              user name : {self.name}
              Age : {self.age}
              Gender :{self.gender}""")
  
#child class
class bank(user):
    def deposit(self, amount):
        self.balance = 0
        self.amount = amount
        self.balance = self.balance + amount
        print("Account balance has been updated  : $ ", self.balance)
  
  
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("insufficient balance l available balnce : $ ", self.balance)
        else:
            self.balance = self.balance - amount
            print("account balance after withdrawl : $", self.balance)
            
    def check_balance(self):
        self.show_details()
        print("account balance after withdrawl : $", self.balance)



a = bank("ritesh", 21, "male")
a.deposit(300)
a.withdraw(100)
a.check_balance()