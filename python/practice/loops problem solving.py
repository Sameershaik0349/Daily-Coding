# n =8
# list =set()
# for i in range (1,n):
#     if n%i==0:
#         list.add(i)
# print(list)

# n =8
# count=0
# for i in range(1,n):
#     if n%i==0:
#         count+=1
# print(count)

# n = int(input("Enter a number: "))

"prime"
# if n <= 1:

#     print("Not a prime number")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")


# n = int(input("Enter a number: "))
# count = 0

# for i in range(1, n ):
#     if n % i == 0:
#         count += 1

# if count == 1:
#     print("Prime number")
# else:
#     print("Not a prime number")

# n = int(input("enter a  number :"))
# count=0
# for i in range (1,n+1):
#     if n%i==0:
#         count+=1
# if count ==2:
#     print("its a prime")
# else:
#     print("not prime")
# # print(count)

"factor"

# n =5
# sum = 1
# for i in range(1,n+1):
#     sum=i*sum
# print(sum)

"perfect"

# n=(int(input("enetr a value:")))
# sum = 0
# for i in range(1,n):
#     if n%i==0:
#         sum =sum+i
# if sum ==n:
#     print("its a perfect number")
    
# else:
#     print("not  a perfect number")

"armstrong"
# start =1

# end =1000
# # length1 = len(str(start))
# # length2 = len(str(end))
# # armstrong=0
# for i in range(start,end+1):
#     length = len(str(i))
#     armstrong=0
#     # armstrong += + i **length
#     # strong = i
#     for x in str(i):
#         x =int(x)
#         armstrong +=x**length


#     if armstrong==i:
#         print(i)



    # armstrong = armstrong + i **length

# a=0
# b=1
# for i in range(6):
#     a,b=b,a+b
# #     print(a)

# h = "Sameer Saheb Sahaik"
# length=len(h)
# vowels="aeiou".lower()
# for i in range(len(h)):
#     if i%2!=0 and h[i] not in vowels:
#         print(h[i])
#         # if h == vowels:
#         #     print("it is in vowels",'==',h[i])


# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))

# for num in range(start, end + 1):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         print(num, end=" ")

# for i in range(10,20):
#     count=0
#     for y in range(1,i):
#         if i%y==0:
#             count+=1
#     if count ==1:
#         print(i)
# print(count)
        
# s =['python','fullstack','java','c++']


# vowels='AEIOU'.lower()
# # count="
# for i in s:
#     count=0
#     for y in i:
#         if y in vowels:
#             count+=1
#     if count>1:
#         print(i)
           
        



# for i in s:
#     temp=int(i)
#     for y in range(s[0][temp]):
#         temp2=int(y)
#         if temp%2==0:
#             print(i)

# for i in range(len(s)):
#     # temp=str(i)
#     if i%2!=0:
#         print(s[i])


# s=122
# l=str(s)
# m=l[::-1]
# if s==int(m):
#     print("its palindrome")
# else:
#     print("not palindrom")


# start =1
# end = 1000
# for i in range(100,1000+1):
#     pali = str(i)
#     m =pali[::-1]
#     if i ==int(m):
#         print(i)
#     # else:
#     #     print("not a palidrom")

# # n = 153
# for i in range(100,500):
#     m = len(str(i))
#     sum=0
#     for x in str(i):
#         sum=sum + int(x) ** m
#     if sum==i:
#         print(sum)

for i in range(1,6):
    for y in range(1,i+1):
        print(y,end="")
    print()
    







