# "modules" 
" --- combinations of varible and functions and classes"
'''
types are 3:-

user define
.py
---------------------------------------------------------
"predefine" ------//bulid in modules   ////software on pyhton
os,path os datetime time

randoms:-
randint ---betw in number
random --number
randuniform ----float betw
random.choice-----char
        
---------------------------------------------
tirdparty
separted installed modules
ex:- pyttsx3,pandas,numpy
install --pip install pandas ---using for install
'''



"use of module"

''' to reuse  a file code in another file
ex-- from "file name" import "varible name"
        print('variable name)

    
'''


"classes"



" "






'''random modules
    to gen randomw numbers
ex:- import random
print(random.random)

ex2:-
for between number 
use - randint -----onlu two urg
print(random.randint(10,20))

ex3:-
mobile number --- valid
print(random.randint(60000000000,999999999))

now randrange ----three urg with steps
print(random.randrange())

'''

# def b_wprime(n):
#     for x in range(0,n):
#         cou=0
#         for j in range(1,x+1):
#             if x%j==0:
#                 cou+=1
#         if cou ==1:
#             print(x)
# b_wprime(n=10)


'''import  random
user=(int(input("guess a number between 1 to 100")))
l=(random.randint(1,5))
if user ==l:
    print("your guess is correct")
else:
    print("try again")
'''
import random
while True:
    player1=((input("press enter")))
    player1=" "
    l1=random.randint(1,10)
    player1+=l1
    player2=((input("pres enter")))
    l2=random.randint(1,10)
    l2=player2
if player1>player2:
    print("player is winner")
else:
    print("player 2 is winner")

