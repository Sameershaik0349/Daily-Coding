""

# scopes

# local ----inside function
#  and
#  global ------- out side of funtion



'''a =10 #global 
b=30
def add1():
    print(a+b)
add1()'''


"we can't update global in inside of function"

'''a =20
b=30
def add2():
    # global a   # so we use global keyword in inside 
    a=200

add2()
print(a)'''


"nested funtions"

'''def outer():#2
    sal=2000#3
    def inner ():#5
        print(sal)#6
    inner()#4
outer() #1
'''

#global   if we want use global in inside function we use global keyword
#nonlocal  if we want to update in inner funtion of a function then we use nonlocal in inner




n=0
while n<=5:
    n+=1
    if n%2==0:
        continue
    print(n)