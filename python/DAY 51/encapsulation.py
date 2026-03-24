"ENCAPSULATION "
# ITS IS USE FOR PROTECTION

#ACCSSES MODIFIERS
# THEY ARE THREE MODIFIERS:
'''
public---name
we can access every where

private --__name
we can only acesses in same class
protected --_name
accese any where



'''
"private"

"updating private varible"
'''class bank():
    __balanace=3500
    def __init__(self):
        self.__balanace+=1000
        print(self.__balanace)
obj=bank()
'''

# "this is exapmple for error becuse we only do in same class no in sub class"

'''class bank():
    __balanace=3500
    def __init__(self):
        # self.__balanace+=1000
        print(self.__balanace)

class sbi(bank):
    def __init__(self):
        bank.__balanace+=1000
        print(bank.__balanace)
obj=bank()
obj =sbi()'''



# 
# name handling --- we can access private vvarrible in outside class
# syntax print(obj._classname__variblename)




# methods in encapculation

# 1.set method
#  2. get method