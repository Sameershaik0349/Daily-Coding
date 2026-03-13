# clas varible

"update in instance"
'''when we update inn instance it goes through boject wise'''
# * instance changes object to object wise
# -----------------------------------------------------------------
"update in class"
"but whne we update in class it see whole class"

# class bank:
#     balance =1000
#     def __init__(slef):
#         bank.balance+=1000
# print(bank.balance)



# class bank2:
#     bal=2000
#     @classmethod
#     def method(cls):
#         cls.bal+=1000
# print(bank2.bal)


class bank():
    name=input("enter your name")
    @classmethod
    def bank1(cls):
        bank.name="sam"
    def delete(cls):
        del bank.name

obj=bank()
ob1=bank()
ob1.delete
print(ob1.name)
obj.bank1()
