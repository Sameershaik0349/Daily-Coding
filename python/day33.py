# l=[10,20,30,40]
# asen=True
# for x in range(len(l)-1):
#     if l[x] > l[x+1]:
#         asen=False
# if asen:
#     print("its ascending order")
# else:
#     print("its descending order")
    

# s =[10,20,30,40]
# sum=0
# count=0
# for i in s:
#     sum+=i
#     count+=1
# print(sum/count)


# s =[10,20,50,43,11]
# asen=[]
# while s:
#     minimum=s[0]
#     for i in s:
#         if i < minimum:
#             minimum = i
#     asen.append(minimum)
#     s.remove(minimum)
# print(asen)


# k=[1,2,4,3,7,6]
# asen=True
# for i in range(len(k)):
#     for j in range(i+1,len(k)):
#         if k[i] > k[j]:
#             k[i],k[j]=k[j],k[i]
        
# print(k)

# k=[1,2,3,4,5,6,7,8]
# target =10
# for i in range(len(k)):
#     for j in range(i+1,len(k)):
#         if k[i] + k[j] == target:
#             print(k[i],k[j])


# k=[10,11,12,13,14,10]
# dup=True
# for i in range(len(k)):
#      for j in range(i+1,len(k)):
#         if k[i] == k[j]:
#             dup=False
#             break
# if dup==True:
#     print("its unique")
# else:
#     print("its not have dup")


# k =[10,20,30,60,70]
# asen=True
# for i in range(len(k)):
#     for j in range(i+1,len(k)):
#         if k[i] < k[j]:
#             k[i],k[j]=k[j],k[i]
# print(k[1])

# k =[10,20,30,40]
# min1=k[0]
# min2=0
# for i in k:
#     if i<min1:
#         min2=min1
#         min1=i
# print(min2)


# k=[10,-12,-8,-9,13,14]
# fin=[]
# for i in k:
#     if i<=0:
#         fin.append(0)
#     else:
#         fin.append(i)
# print(fin)

# # k=[1,0,1,0,1,1,0,0,1]
# # new=[]
# # ones=[]
# # for i in k:
# #     if i<=0:
# #         new.append(i)
# #     if i >0:
# #         ones.append(i)
# # print(new+ones)



# k=[1,0,1,0,1,1,0,1,0,1,1,0]
# for i in range(len(k)):
#     for j in range(i+1,len(k)):
#         if k[i] > k[j]:
#             k[i],k[j]=k[j],k[i]
# print(k)
        
# Find the second largest and second smallest number in a list.

lis=[10,20,30,40,50,90,60]
max1=lis[0]
max2=lis[0]
min1=lis[0]
min2=float('inf')
for i in lis:
    if i > max1:
        max2=max1
        max1=i
    elif i >max2 and i!=max1:
        max2=i
    if i < min1:
        min2=min1
        min1=i
    elif i < min2 and i!=min1:
        min2=i
print("max2",max2)
print("max1",max1)
print("mmin1",min1)
print("min2",min2)



# for i in range(len(lis)-1):
#     for j in range(i+1,len(lis)):
#         if lis[i]>lis[j]:
#             lis[i],lis[j]=lis[j],lis[i]
# print(lis)