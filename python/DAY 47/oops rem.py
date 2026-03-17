# STATIC METHOD
#  it dont any paramter like slef or cls only with decorator 
'''class bank:
    @staticmethod
    def create_acc():
        pass
'''

"local varibles"
# we only updat or del or print for a local varbile in their function only


# function

#  SUPER() ---TO acceses from parent features in child
# *when method over ridding
# * when we have same funtions like constructor,methods in two classes then there wll be over ride


'''class parent:
    def __init__(self):
        print("this is parent")
class child(parent):
    def __init__(self):
        super().__init__()
        print("this is child class")
obj = child()'''


# ex-2
'''class clg:
    def __init__(self,acc_no):
        self.acc_no = 10
        print(self.acc_no)
'''


# ex3

'''class school:
    def __init__(self,school_name,head):
        self.school_name= school_name
        self.head =head
class teacher (school):
    def __init__(self,teacher_name,teacher_age,school_name,head):
        self.teacher_name = teacher_name
        self.teacher_age =teacher_age

        print("teacher_name:-",self.teacher_name)
        print("teacher_age:-",self.teacher_age)

        super().__init__(school_name,head)
        print("school_name:-",self.school_name)
        print("head_name:-",self.head)


obj=teacher("vinay",21,"vinay raja",'veeresh')'''



class school:
    def __init__(self,head_name,departments):
        self.head_name=head_name
        self.departments=departments
class teachers(school):
    def __init__(self, head_name, departments,teacher_name,techer_age):
        self.teacher_name =teacher_name
        self.techer_age=techer_age
        school.head_name=head_name
        school.departments=departments


        print(school.head_name)
        print(school.departments)
        print(self.teacher_name)
        print(self.techer_age)
obj=teachers("sameer","aiml","shaik",17)



        
