# "complex"


# l=2+3j

# print(l.real)


# k=12
# for x in range(k):
#     print(x)

"non primitive"

# list, tuple, dict,set,



'LIST'


# l=['sameer','number','saheb',10000,'coders',2+3j] #----->  #hetrogenius objects   # its also dulipcate because its 
# l[5]='Shaik'
# l[0]='tobi'  #upadate
# l.append('sameeeeer') #append or     ( k+=['sameeer'])
# l.remove(10000)     # remove
# l.insert(1,'sammerrrrrrr')   #insert at  any position
# print(l)  
# print(type(l))
# print(l[0])   #indexing
# print(l[1:5])    #slicinh
# print(len(l))

# # a=5
# # b=9
# # a,b=b,a
# # print("a=",a)
# # print("b=",b)






# k =['sameer','saheb',10000,'coders']
# k[0]='saheb'
# k.append('sameeeer')
# k.remove("saheb")
# k.insert(1,'sameeeeer')

# print(k)

# import time
# res=tuple() 
# print('data type:',type(res)) 
# print('id:',id(res)) 
# time.sleep(2) 
# print(res)

"tuple"
# sameer=('sameeer','saheb',(11000000,'sameeeeeer'))
# print(sameer[2])
# print(sameer[2][1][0:3])


"set"

# sameer={'sameeeeer','saheb',10000000,(1112,'Sam'),'hii'}
# sameer.add(100)
# sameer.remove('sameeeeer')
# sameer.update({'salma','hyma'})
# print(sameer)


"dic"


# hello=('sameeer',{'kumar':1234567890,'kumar2':56787654})
# print(hello[1]["kumar"])












"primitive"
"INT DATA TYPE"
"Feature: Stores whole numbers"
# a = 10
# b = -5
# c = 0
# print(a, b, c)
# print(type(a))

# "Feature: Supports binary, octal & hexadecimal"
# x = 0b1010
# y = 0o123
# z = 0x1A
# print(x, y, z)

# "float"

# x = 10.5
# y = 3.5e2
# print(x, y)
# print(type(y))

# "COMPLEX DATA TYPE"
# "Feature: Real & Imaginary Parts"
# c = 3 + 4j
# print(c.real)
# print(c.imag)

# "Feature: Arithmetic operations"
# a = 2 + 3j
# b = 1 + 2j
# print(a + b)

# " BOOLEAN DATA TYPE"
# "Feature: Result of comparison"
# print(10 > 5)
# print(5 == 10)

# "Feature: Subclass of int"
# print(int(True))
# print(int(False))

# "STRING DATA TYPE"
# "Feature: Immutable & Indexed"
# name = "Sameer"
# print(name[0])
# print(len(name))

# "Feature: Multi-line string"
# text = """Hello
# Python"""
# print(text)


# "non primitive"

# "LIST"

# "Feature: Mutable & Ordered"
# l = [10, "apple", 3.5]
# l[1] = "mango"
# print(l)


# "Append"
# l = [10, 20, 30]
# l.append(40)
# print(l)

# "Insert"
# l.insert(1, 15)
# print(l)

# "Remove"
# l.remove(20)
# print(l)

# l[0]=59                 # this for updating 
# print(l)

# "TUPLE"
# t = (10, 20, 30, 40)
# print(t)

# "Indexing"
# print(t[2])

# "Slicing"
# print(t[1:3])

# "Count duplicate values"
# t = (10, 20, 20, 30)
# print(t.count(20))


# "SET"
# "Add"
# s = {10, 20, 30}
# s.add(40)
# print(s)

# "Remove"
# s.remove(20)
# print(s)

# "DICTIONARY"

# d={"sameer":123456789}
# print(d)

# "Add"
# d = {"name":"Sam", "age":21}
# d["city"] = "Hyderabad"
# print(d)

# "Update"
# d["age"] = 22
# print(d)

# "Remove"
# d.pop("city")
# print(d)

"arthmetic"
"multiplication"
# a =[10,20]
# v=2
# print(a*v)

'set'

# a ={10,20,30}
# b=3                       # for list
# print(list(a)*(b))

# "assignment"      ==> +=,*=,%=,-=,**=,/=,//=
# a=12
# b=12
# a=a+b  #or a+=b     no need to declare third variable
# print(a)


"special operators"
# two  types
'membership -->' #To check  there or not with --> 'in & not in'

# members=['sameer','shaik','tobi']
# res ='saheb' in members
# res1='sssss' not in members
# print(res1)     # then it is false
# print(res)         #true

'identity operator -->'  #To check address of two varibles     upto 256 it stores in same adress    (is---and is not  for id)       and       ('==' is check the values only not add)
# a=257
# b=257
# print(a is b)

"conditional statments"

# n=0

# if n>=0:
#     print("positive")
#     print("or zero")
# elif n<0:                     "onece the condition is true then it does't run or go to the next condition"
#     print("negitive")
#     print("dont go to else")
# else:
#     print("zero")


"find marks grads"
# n =90                               
# if n>=90:
#     print("a+")         |
# if n>=90:               |   check all conditions  
#     print('a')          |

"finding largest value in two variables"
# a=100
# b=20
# if a>b:
#     print("max value is :",a)
# elif a<b:
#     print("max value is:",b)


" "

# a=12
# b=13
# if a>b:
#     print(a)
# elif b>a:
#     print(b)

" "

# a=int(input("enter your age:"))
# if a<18:
#     print("he is not eligble")
# elif a>=18:
#     print("yes he is eligible to vote")





# n=input("enter a letter:")
# # vow='AEIOU'.lower()
# vow=['A','E','I','O','U']
# if n in vow:
#     print("its vowel letter")
# else:
#     print("it's not a vowel")

" "
# user=int(input("eneter a num:"))
# if user%3==0 and user%5==0:
#     print("yes it's divisble by 3&5")
# elif user%3==0:
#     print("yes its divible by 3")
# elif user%5==0:
#     print("yes uts divisble by 5")
# else:
#     print("the given number is not divisble iwth 3&5")


# import keyword
# print(keyword.kwlist)


"Conditional Statments"

" Check whether a number is positive or negative "

# user=int(input("enter a num :"))
# if user<0:
#     print("its neg number")
# elif user>0:
#     print("its posituve number")
# else:
#     print("zero")


"Check whether a number is even or odd."

# user = int(input("enter a num:"))
# if user%2==0:
#     print("its even number")
# else:
#     print("its odd number")

"Check whether a number is divisible by 5."
# user = int(input("enter aa value:"))
# if user%5==0:
#     print("yes its divisble by 5")
# else:
#     print("its not divisble by 5")

"Find the greater of two numbers."

# a=11
# b=10
# if a>b:
#     print("a is greater than b :",a)
# elif b>a:
#     print("b is greater than a :",b)

"Find the greatest of three numbers"

# a =10
# b=50
# c=60
# if a>b and a>c:
#     print("a is greater than b&C")
# elif b>a and  b>c:
#     print("b is greater than a & c")
# elif c>a and  c>b:
#     print("c is greater than a&b")

"Check whether a year is a leap year."

# year =int(input("enter a year"))
# if year%400==0:
#     print("ye it is a leap year")
# elif year%4==0 and year%100 !=0:
#      print("yes it is a leap year")
# else:
#     print("its not a leap year")


"Check whether a person is eligible to vote."


# age=int(input("enter you age :"))
# if age<18:
#     print("no your not eligible")
# elif age>=18:
#     print("yes your eligible")

"Check whether a character is a vowel or consonant."

# user=input("enter a letter :")
# vowels='AEIOU'.lower()
# if user in vowels:
#     print("its vowel letter")
# elif user not in vowels:
#     print("its  a consonant")

"Check whether a number is divisible by both 3 and 7."

# user = int(input("enter a value"))
# if user%3==0 and user%7==0:
#     print("yes its divisble by 3 & 7")
# else:
#     print("not divisble ")

"Check whether a number is single-digit, double-digit, or more"

# user= int(input("enetr a value"))
# if -9<= user <=9:
#     print("its a single digit")
# elif -99<= user <=99:
#     print("its a double digit")
# else:
#     print("its more than double digit")

# elif user>=99 and user <=999:
#     print("its a thribble digit")




# n =int(input("enter a number:"))
# if n>0:
#     s1=n//500
#     print(s1,"500 notes")
#     # print(n)
#     n%=500  
#     # n = n%500
# # print(n)
# if n>0:
#     s2 =n//200
#     print(s2,'200 notes')
#     n%=200
# if n>0:
#     s3 =n//100
#     print(s3,'100 notes')
#     n%=100
# if n>0:
#     s4 =n//50
#     print(s4,'50 notes')
#     n%=50
# if n>0:
#     s5 =n//20
#     print(s5,'20 notes')
#     n%=20
# if n>0:
#     s6 =n//10
#     print(s6,'10 notes')
#     n%=10
# if n>0:
#     s7 =n//5
#     print(s7,'5 rupee coin')
#     n%=5
# if n>0:
#     s8=n//2
#     print(s8,'2 rupee coin')
#     n%=2

# if n>0:
#     s9 =n//1
#     print(s9,'1 rupee coin')
 


# n=403
# if n>0: 
#     y=n//365 
#     print(y,'year') 
#     n%=365 
# if n>0: 
#     y1=n//30 
#     print(y1,'month') 
#     n%=30 
# if n>0: 
#     y2=n//7 
#     if y2>0: 
#         print(y2,'week') 
#     n%=7 
# if n>0: 
#     print(n,'days') 



# salary = int(input("enetr  salary :"))
# if salary <= 250000:
#     print("no tax")
# elif salary  <= 500000:
#     s1 = (salary - 250000) * 0.05
#     print("tax",s1)
# elif salary  <= 1000000:
#     s2 = (250000 * 0.05) + (salary - 500000) * 0.20
#     print("tax",s2)

# else:
#     s3 = (250000 *0.05) + (500000 *0.20) + (salary -1000000)*0.30
#     print("tax",s3)
