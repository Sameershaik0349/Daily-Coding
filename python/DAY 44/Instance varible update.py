"instance varible"

"update method"


"in construction or instance"

'''class empolyee:
    def __init__(self):
        self.balance=1000
    def updte(self):
        self.balance+=1000
obj=empolyee()
obj.updte()
obj.balance+=1000 #----updating outside class
print(obj.balance)'''



"subclasss"

'''class bank1():
    def __init__(self):
        self.emp_name="sameer"
class sam(bank1):
        def pr(self):
            print(self.emp_name)
obj1=bank1()
obj=sam()
obj.pr()'''


"delete"


'''class bank():
    def __init__(self):
        self.emp_name="sameer"
        del self.emp_name
obj=bank()
print(obj.emp_name)'''



'''class bank():
    def __init__(self):
        self.emp_name="sameer"
    def sam(self):
        del self.emp_name
        
obj=bank()
obj.sam()
print(obj.emp_name)'''


"sub class update"
'''class bank1():
    def __init__(self):
        self.emp_sal=100
class sam(bank1):
        def pr(self):
            self.emp_sal+=100

obj=bank1()
obj1=sam()
obj1.pr()
print(obj1.emp_sal)'''
# ----------------------------------------------------------------------------------


"Class method"

'''
*object ot object can not change
* it decalre in inside class method

* we use class attrib fr call only class details
'''

'''class bank:
     @classmethod
     def create_account(cls):
          cls.bal=100
obj=bank()
obj.create_account
print(bank.__dict__)'''


"class variable"
'''Declare in only'''
# inside class
# outside method


'''class emp():
    name ="sameer"
    pin=101
    def method():
        pass
obj=emp()
print(emp.__dict__)
'''

"inside constructor"

'''class emp1():
    def __init__(self):
        emp1.name="sameer"
obj=emp1()
print(emp1.__dict__)'''


"inside clsss"

'''class bank():
    @classmethod   # it is decoarter   .....by this we know this is class method
    def cls_method(cls):
        cls.emp_name="samee"
        cls.acc_num=12345678
        print(cls.emp_name)
# obj=bank()
# obj.cls_method()
# print(bank.__dict__)

bank.cls_method()'''