# class sam():
#     def even(self):
#         for x in range(1,10):
#             if x %2==0:
#                 print(x)

# sum1 = sam()  
# sum1.even()

# "oops"

# # 'class' -- blue print

# class classname:
#     pass

# # "object   we can create no of objects to class

# obj = classname () 
# obj1 = classname()


class employee:
    __emp_id=101  # protecttedd   or privated
    emp_name='sameer'
    emp_age=12
    emp_salary=2500
    def __details(self): # private method
        print(self.__emp_id)
        print(self.emp_name)
        print(self.emp_age)
        self.emp_salary+=10    #  updatingggg
        print(self.emp_salary)

    def m1(self):
        self.__details()


c1=employee()
c1.m1()
print(c1.m1())

# c1.details() 
# print(c1.__emp_id) #--------only inner function only can get this output    
# we can't call this from outside class


