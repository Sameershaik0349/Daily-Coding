"inheritence"
# a class extend from another class
# 5 types
'''
single --on class form one claas
mul  -one child contains mul parents
mul level -- a child inherits from parent,and another child inherit from that child
herarical --mul childc lases contais same parent class
hybrid  ---a combination of morethan one type of inheritance
'''


# SINGLE INHERITENCE

class grandfather:
    def __init__(self):
        self.name="mast"
class parent(grandfather):
    def p1_1(self):
        self.p1_="mastan"
class parent2():
    def p2_2(self):
        self.p2="phirani"
class child(parent,parent2):
    def child_1(self):
        self.child_name="salma"

obj=grandfather()
print(obj.name)

        