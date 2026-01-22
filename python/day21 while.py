# for i in range(1,5):
#     for y in range(1,11):
#         print(i,'x',y,'=', i * y)
#     print()

# n ="saa"
# count=""
# for i in (n[::-1]):
#     count+=i
# if count == n:
#     print("its palindrom")
# else:
#     print("not a palindrom")  
# print(count)
    
# for x in range (1,6):
#     for y in range (1,3):
#         print("*" *x , "*" * y,end =" ")
#     print()
# for i in range (5,0,-1):
#     print("*" *i)
# for i in range(70,65,-1):
#     for y in range(65,i + 1):
#         print(chr(y),end =" ")
#     print()
# "while loop"------ until this conition is true it work as loop -----if we know the no of itearations then use for loop if dont know use while***
# a =1
# while a<=10:
#     print(a)
#     a+=1


# a= -10     
# while a<=-1:
#     print(a)
#     a+=1

# a =123
# while a ==123:
#     a=str(a)
#     print(a[::-1])

# a =121
# b=a
# rev=0
# while a>0:
#     d=a%10
#     rev= rev * 10 + d
#     a//=10
# if b == rev:
#     print("its palindrome")
# else :
#     print("not palindrom")
# else:
#     print("its not a palindrom")
#     if a == rev:
#         print("its palindrom")
# else :
#     print("its not a palindrom")



# a =24356
# # h=a
# count=0
# # h=a
# new=0

# while a>0:
#     d=a%10
#     new+=d
#     a//=10
#     if new%d==0:
#         count+=1
# if count==1:
#     print("its a prime")
# else:
#     print("not a prime")
# print(count)

num = 4
i = 1
count = 0

while i <= num:
    if num % i == 0:
        count += 1
    i += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")
