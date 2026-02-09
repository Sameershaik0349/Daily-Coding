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
# neg=[]
# for i in k:
#     if i>0:
#         neg.append(i)
# print(neg)

# # k=[1,0,1,0,1,1,0,0,1]
# # new=[]
# # ones=[]
# # for i in k:
# #     if i<=0:
# #         new.append(i)
# #     if i >0:
# #         ones.append(i)
# # print(new+ones)



k=[1,0,1,0,1,1,0,1,0,1,1,0]
for i in range(len(k)):
    for j in range(i+1,len(k)):
        if k[i] > k[j]:
            k[i],k[j]=k[j],k[i]
print(k)
        

