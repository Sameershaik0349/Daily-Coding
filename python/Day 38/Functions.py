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




'''n=0
while n<=5:
    n+=1
    if n%2==0:
        continue
    print(n)'''

'''def is_prime(n):
    if n <= 1:
        return "Not Prime"
    
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"

print(is_prime(4))'''

'''
def sort_list(arr):
    
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
    return arr

print(sort_list([5,2,8,1,3]))'''



def binary_search(arr, target):
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1
            
    return -1

print(binary_search([1,2,3,4,5,6,7], 5))