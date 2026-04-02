'''

AREA OF SQARE:-

FORMULA -side * side

1.creating varible side 
2.dtat type float
Steps:-
1.input from user
2.store it ina varible
3.caluculate area ///area =side*side















'''


# user=float(input("enter the side"))
# area=user*user
# print(area)

"optimized code"

# use function for reusbility when doing dsa problems

# def sqare():
#    sides=float(input("enter the side"))
#    return sides**2
# print(sqare())

# understand data structture
# always use functions
# optimize the time
# the no of times you reference to a varible the memory gets allowed
# varible is a address


'''
Area of rectangle

formula --length *breadth
'''
# length = float(input("enter a legnth"))
# Breadth = float(input("enter a breadth"))
# area=length*Breadth
# print(area)


# def area(length:float,breadth:float):   #type casting
#     if length==0 or breadth==0:
#         return ("invalid")
#     return float(length*breadth)

# print(area(6,0))


"amount sum"
def satm(amount):
    thousands=amount//1000
    reming_change=amount%1000
    fives=reming_change//500
    fin=reming_change%500
    print(f"thousands={thousands},five hunders ={fives},change={fin}")
satm(3700)