# ==============GENRATOR=====
# IT IS GENRATE ONCE A TIME A VALUE WILL STORE 
# USE FOR MEMORY EFFICIENCY
# WHEN WE CALL THEN ONLT STORE
# USE WHEN WE USING LARGE DATA SET
# THEY ARE  2WAYS TO CREATE GENRATOR
# IN TUPLE COMPERHENSION'''
#  whn we call then only store
#genrator does not support index values


# TYPE 1
'''RES =(x for x in range(100))
for x in RES:
    print(x) '''# when we want print all values use this
# print(RES)
# print(type(RES))
# print(next(RES))#----for first value
# print(next(RES))#---next value



# TYPE 2
def num():
    for x in range(10):
        if x%2==0:
            yield x # it denotes this is genrator not a function

'''obj=num()
print(next(obj))
print(next(obj))''' #this is correct method to print genrator method
# print(next(num()))
# print(next(num()))



"between prime numbers"


'''def prime(a,b):
    for x in range(a,b):
        for j in range(2,x):
            if x%j==0:
                break
        else:
            yield x


obj=prime(20,30)
# print(next(prime(20,30)))
for z in obj:
    print(z)
'''




# def num():
#     yield 1
#     yield 2
#     yield 3

# obj=num()
# print(next(obj))
# print(next(obj))
# print(next(obj))
# ------------------------------------------------------

# def table(a):
#     for x in range(1,11):
#         yield f"{a} * {x} = {a*x}"

# obj=table(2)
# # print(next(obj))
# # print(next(obj))

# for x in obj:
#     print(x)



import zipfile


    

