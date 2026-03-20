class account:
    def details(self,user_name,user_acc_no,user_acc_bal):
        print("=============details===============")
        self.user_name=user_name
        self.user_acc_no=user_acc_no
        self.user_acc_bal=user_acc_bal
        print(user_name, user_acc_no, user_acc_bal)
        print("=============details===============")
        
    def deposit(self,amount):
        if amount>0:
            self.user_acc_bal+=amount
            print("=============deposit===============")
            print("deposited succesfull:-",self.user_acc_bal)
            print("=============deposit===============")
    def withdraw(self,amount):
        if amount>0:
            if self.user_acc_bal<amount:
                print("insufficent bal :-",self.user_acc_bal)
            else:
                self.user_acc_bal-=amount
                print("=============withdraw===============")
                print("withdraw successfull:-",self.user_acc_bal)
                print("=============withdraw===============")
        else:
                print("Please enter valid amount")
    def check_bal(self):
        print(self.user_acc_bal)

import random;
user_name=input('Enter your name :- ')
user_acc_no= print(random.random)
user_acc_bal=float(input("Enter initial balance :- "))
obj=account()
obj.details(user_name, user_acc_no, user_acc_bal)
while True:
    print("For deposit press 1")
    print("if for withdraw press 2")
    print("if for check_bal press 3")
    print("if for details press 4")
    print("if exit press 5")

    procces=int(input("Enter a process number :-"))
    if procces==1:
        amount=float (input("Enter a amount :- "))
        obj.deposit(amount)

    elif procces ==2:
            amount=float(input("Enter withdraw amount :-"))
            obj.withdraw(amount)
    elif procces==3:
        obj.check_bal()

    elif procces==4:
        obj.details(user_name, user_acc_no, user_acc_bal)
         
    elif procces ==5:
        print("Thank you for visting")
        break
    




