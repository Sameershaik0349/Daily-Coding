
def add1(a,b):
    print(a+b)
"add1(20,30)"  # in this we can't get more than 2 urguments


# "varible length arugument" ---- to perform number of arguments

'''def vla(*a): #tuple datatype
    print(sum(a))
vla(10,20,30)

def add(*a):
    sum1=0
    for i in range(len(a)):
        sum1+=a[i]
    print(sum1)

add(20,30)'''



"ex2"
# def employee(name,pin,*dep,salary =5000):
#     print("employee name :",name)
#     print


# "keyword varible length urgument"
# def st(**a):     # dic type
#     print(a)

# st(name="kum",pin=101,age=15)


# def st1(**a):
#     for k,v in a.items():
#         print(k ,"=" ,v)


# st1(name="kum",pin=101,age=15)

# def st2(name,pin,*a,**b):
#     print("name",name)
#     print("pin",pin)
#     print("a",a)
#     print("b",b)
# st2("sameer",13,10,name1= "sam",age =12)


'''def cal():
    val1=int(input("enter a val 1 :"))
    val2=int(input("enter a val 2 : "))
    operator = (input("enter  a operator"))
    if operator == "+":
        print(val1+val2)
    elif operator == "-":
        print(val1 -val2)
    elif operator == "*":
        print(val1*val2)
    elif operator == "//":
        print(val1//val2)
    else :
        print("invalid opertor")
cal()
'''


'''
def palin():
    # i=input("enter  a name")
    l = ["madam"]
    tem=l
    tem1=""
    for i in l:
        tem1 = i +tem1 
    tem1=tem
    if tem==l:
        print("its palindrom")
    else:
        print("not a palindrom")
palin()

"nested function"'''

def user_prime(a):
    user=int(input("enter a number"))
    lower=user
    upper=user
    while True:
        if user> upper:
            user-1
        elif user < lower:
            user+1
        











