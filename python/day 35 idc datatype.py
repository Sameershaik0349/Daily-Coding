"dict data types"
# its mutable datatype


# d={}
# print(d)
# print(type(d))


# d ={"sameer":234567}
# d.update({"sameer2":2})
# d['mobile']=123456789
# d.pop('mobile')# pop randomly
# d.popitem() # default remove last number
# print(d.get("sameer")) # tooo get sepcfic value
# print(d["sameer"]) # without get
# items for keys and values
# print(d)

# its iterable

# d={"a":123,"b":233,"c":56}
# for i in d:
# #     print(i)
# for k,v in d.items():
#     print(k,v)



# ste_re=[{"id":101,"std_name":"shaik","mobile":1234567},
#         {"id":102,"std_name":"shaik","mobile":12345678}]
# d =102
# for i in ste_re:
#     if i["id"]==d:
#         for k,v in i.items():
#             print(k,"=",v)


# id=(input("enter your id:"))
# std_name=(input("enter your name:"))
# std_mobile=(input("enter your mobile number:"))
# store={}
# for i in id:
#     store["id"]=(id)
    
#     for x in std_name:
#         store["std_name"]=(std_name)
        
#     for j in std_mobile:
#         store["std_mobile"]=(std_mobile)
            
# print(store)


# h= dict([('a',10),('b',20)])
# print(h)



# exchange keys and value
'''j ={'name':'ajay','mobile':1234567}
tem={}
for k,v in j.items():
    tem[v]=k
print(tem)'''

# words=["apple","banana","kiwi"]
# temp={}
# count=0
# for i in words:
#     for  j in range(a,d):
#         temp[i]=len(i)
#     print(temp)


# words = ["apple", "banana", "kiwi"]
# temp = {}

# for word in words:
#     temp[word[0]] = len(word)

# print(temp)
# 
# words = ["apple", "banana", "kiwi"]

# temp={}
# for i in words:
#     count=0
#     for j in i:
#         count+=1
#     temp[i]=count
# print(temp)



"factors of values "
'''j =10
fac=[]
result={}
for i in range(1,j):
    if j%i ==0:
        fac.append(i)
    tem=result[j]=fac

print(result)'''

# for mutliple value
'''j =[12,8,10]
result={}
for i in j:
    fac=[]
    for x in range(1,i):
        if i%x==0:
            fac.append(x)
    tem=result[i]=fac
        
print(result)'''


# range=4
# output {2:(s:4,)}
# temp={}
# for i in range(1,4):
#     squre=[]
#     cube=[]
#     squre1=i **2
#     squre.append(squre1)
#     cube1= i**3
#     cube.append(cube1)
#     temp[i]=(squre,cube)

# print(temp)


# even oddd
# k = [10, 11, 12, 13, 14, 15]
# d = {}

# for i in k:
#     if i % 2 == 0:
#         d[i] = "even"

#     else:
#         d[i]='odd'
# print(d)


# keys=['name','age','city']
# values=['jhon',25,'newyork']
# res={}
# for i in range(len(keys)):
#     res[keys[i]]=[values[i]]
# print(res)

# prime problem

j=[11,12,13,14]
temp={}
for i in j:
    count=0
    for x in range(1,i):
        if i%x ==0:
            count+=1
    if count==1:
        temp[i]="prime"
    else:
        temp[i]="not a prime"
print(temp)

''''j = [11, 12, 13, 14]
temp = {}

for n in j:
    if n < 2:
        temp[n] = "not a prime"
        continue

    for i in range(2, n):
        if n % i == 0:
            temp[n] = "not a prime"
            break
    else:
        temp[n] = "prime"

print(temp)
'''

# d ='sucess' 
# cou={}
# for i in d:
#     if i not in cou:
#         cou[i]=1
#     else:
#         cou[i]+=1
    
# print(cou)





