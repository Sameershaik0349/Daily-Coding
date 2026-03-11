"instance varible "

"using constructor"
'''class employee:
    def __init__(self):
        self.emp_name=input("enter your name:-")
        self.emp_id=(int(input("enter your id:-")))
    

obj = employee()'''


"instance method"

class emp:
    def method(self):
        self.emp_name=input("enter your name:-")
        self.emp_id=(int(input("enter your id:-")))

    

obj1 = emp()
obj1.method()

"outer class"

obj1.emp_name="sameer"
print(obj1.emp_name)