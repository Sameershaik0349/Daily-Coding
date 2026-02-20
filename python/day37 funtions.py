"Functions"  # if we wnat to reuse the code in 200 lines codes then we can use functions

# def even():
#     for i in range(2,40,2):
#         print(i)
# even()


# even() # reusing the function  


# def add(x,y):
#     c=x+y
#     print(c)
# add(1,1)

def mul_sub(x,y):
    e = x-y
    d=x*y
    return e,d
result1,result2=mul_sub(1,1)
print(result1,result2)

