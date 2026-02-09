# # def even():
# #     for i in range (10,31):
# #         if i%2==0:
# #             print(i)

# # even()


# # a=5
# # if a%2==0:
# #     print(a)
# # else:
# #     print('no its not a even')



# # for i in range (1,100):
# #     if i%2==0:
# #         print(i)


# c=0b10101
# print(c)
# t=int (input("88888"))
# print(t)


# d={'sameer':{'telugu':123,'hin':12334,'eng':1234567}}
# for k,v in d.items():
#     print(k,v)
# # d.update({'age':1234567}) 
# # d['salary']=12345    #without update
# # print(d)
# # d.pop('sameer')           #remve
# # print(d)



# # print(d['sameer']["hin"])

# "operators"




# marks = []
# for i in range(5):
#     marks.append(int(input(f"Enter marks of subject {i+1}: ")))

# if any(m < 40 for m in marks):
#     print("Fail")
# else:
#     percentage = sum(marks) / 5
#     if percentage >= 75:
#         grade = "A"
#     elif percentage >= 60:
#         grade = "B"
#     elif percentage >= 50:
#         grade = "C"
#     else:
#         grade = "D"
# print("Pass")
# print("Percentage:", percentage)
# print("Grade:", grade)

# m1=(int(input("enter marks =")))
# m2=(int(input("enter marks =")))
# m3=(int(input("enter marks =")))
# m4=(int(input("enter marks =")))
# m5=(int(input("enter marks =")))
# if m1 <40 or m2<40 or m3<40 or m4<40 or m5<40 :
#     print("fail")
# else:
#     print('pass')
#     print(m1+m2+m3+m4+m5/5)


# n = 8 
# cou=0
# for i in range (1,n):
#     if n%i==0:
#         cou=cou+1
# print(cou)



# n =8
# cou=0
# # perfect = 8
# for i in range (1,n):
#     if n%i==0:
#         cou+=i
# if cou == n:
#     print("yes it is perfect number")
# else:
#     print("not a perfect number ")



# n =153
# length=len(str(n))
# armstrong=0
# for i in (str(n)):
#     i =int(i)
#     armstrong+=i**length
    
# print(armstrong)

# start =1
# end =1000
# for i in range(start,end +1):
#     length=len(str(i))
#     temp =0
#     i = int(i)
#     temp +=i**length
#     for m in str(i):
#         temp +=int(m)**length
# print(length)


# "Find the sum of digits of a number"

# num = input("Enter number: ")
# total = 0

# for d in num:
#     total += int(d)

# print(total)

# "Output: Sum of digits"

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
# print(count)







    




    
    
        