class account:
    def details(self,user_name,user_acc_no,user_acc_bal):
        print("=============deatails===============")
        self.user_name=user_name
        self.user_acc_no=user_acc_no
        self.user_acc_bal=user_acc_bal
        print(user_name, user_acc_no, user_acc_bal)
        print("=============deatails===============")
        
    def deposit(self,amount):
        if amount>0:
            self.user_acc_bal+=amount
            print("=============deposit===============")
            print("deposited succesfull:-",self.user_acc_bal)
            print("=============deposit===============")
    def withdraw(self,amount):
        if self.user_acc_bal<amount:
            print("insufficent bal :-",self.user_acc_bal)
        else:
            self.user_acc_bal-=amount
            print("=============with draw===============")
            print("withdrww sucess full:-",self.user_acc_bal)
            print("=============with draw===============")
    def check_bal(self):
        print(self.user_acc_bal)


user_name=input('enter your name :-')
user_acc_no=int(input("enter your acc number:-"))
user_acc_bal=float(input("emter initial bal"))
obj=account()
obj.details(user_name, user_acc_no, user_acc_bal)
while True:
    print("if for deposit press 1")
    print("if for with draw press 2")
    print("if for check_bal press 3")
    print("if for details press 4")
    print("if exit press 5")

    procces=int(input("enter a process num"))
    if procces==1:
        amount=float (input("enter a amount"))
        obj.deposit(amount)

    elif procces ==2:
            amount=float(input("enter withdraw amount"))
            obj.withdraw(amount)
    elif procces==3:
        obj.check_bal()

    elif procces==4:
        obj.details(user_name, user_acc_no, user_acc_bal)
         
    elif procces ==5:
        print("thank you for visting")
        break
    




