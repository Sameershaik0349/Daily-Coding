# for x in range(100,1000):
#     f=x
#     tem=0
#     while x>0:
#         d=x%10
#         x//=10
#         tem= tem*10+d

#     if  f==tem:
#         print("its palindrom",tem)


# f =153
# n=f
# f2 = len(str(f))
# t =0
# while f>0:
#     d = f%10
#     t = t + d ** f2 
#     f//=10
# print(t)
# if n == t:
#     print("its a armstrong number")
# n=1
# a,b=0,1
# for x in range(5):
#     print(a)
#     a,b=b,a+b
#     # n+=1

# n=1
# a,b=0,1
# while n<=11:
#     print(a)
#     a,b=b,a+b
#     n+=1

# n =2834
# great=0
# while n>0:
#     d=n%10
#     if d>great:
#         great = d
#     n//=10
# print(great)


# n =2834
# min =9 
# while n>0:
#     d=n%10
#     if d<min:
#         min = d
#     n//=10
# print(min)


# a=5
# while a<=10:
#     b = 0 
#     while b<=12:
#         print(a,"x",b,"=",a*b)
#         b+=1
#     print()
#     a+=1


a ="python"
n = 0
while n < len(a) -1:
    print(a[n])
    n+=1