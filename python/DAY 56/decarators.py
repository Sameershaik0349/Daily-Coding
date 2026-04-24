# DECARATORS

# did not changing original code and etending the the code with out distubing main code


# ?WITH PARAMETERS
'''def even(check_num):
    def inner(b):
        if b%2==0:
            print("even")
        else:
            print("odd")
    return inner



@even
def check_num(a):
    print(a)

check_num(10)'''


# pprime number by using decarator
def prime(check_num):
    def inner(a,b):
        for x in range(a,b):
            for j in range(2,x):
                if x%j==0:
                    break
            else:
                print(x)
    return inner

@prime
def check_num(a,b):
    for x in range(a,b):
        print(x)


check_num(10,20)

# authentication
'''def secure(user):
    def inner(a,b):
        if a=="sameer" and b=="1234":
            print("login sucess")
        else:
            print("wrong credentials")
    return inner

@secure
def user(username,password):
    print(username)
    print(password)



user(a="sameer",b='1234')'''


# execution time
'''import time
def time1(fun):
    def inner():
        s=time.time()
        fun()
        b=time.time()
        time2=b-s
        print(time2)
    return inner
        

@time1
def fun():
    for x in range(10):
        time.sleep(1)
        print(x)


fun()'''
# def deca1(fun):
#     def inner():
#         print("d1")
#         fun()

#     return inner
# def deca2(fun):
#     def inner():
#         print("d2")
#     return inner


# @deca1
# @deca2
# def fun():
#     print("mul")


# fun()


# PDBC  ==>python database connection
'''conneting python with database'''
