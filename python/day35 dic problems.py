'''res ={'a':10,'b':20,'c':30}
sum=0
for i in res.values():
    sum+=i
print(sum)
'''
'''user=(int(input("eneter a values")))
l =[]
for i in range(2,100):
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        l.append(i)
    if len(l)==user:
        print(l)
        break'''


# user=int(input("enter a value:"))
# p=2
# cou=0
# while user>cou:
#     is_prime=True
#     for i in range(2,c)




'''words = ["cat", "dog", "bat"]
rev = {}

for i in words:
    temp = ""
    for j in i:
        temp = j + temp   
    rev[i]=temp

print(rev)
'''

'''
re={}
for i in range(65,91):
    re[chr(i)]=i
print(re)
'''
'''
user=input("enter a one char :")
vow1="aeiouAEIOU"
vow={}
if user in vow1 and user.isalpha():
    temp=user.upper()
    vow[temp]=ord(temp)
    print(vow)
else:
    print(user)

'''

'''d1={'a':1,"b":2}
d2 ={'c':3,'d':4}

res={**d1,**d2}
print(res)'''

'''d1={'a':1,"b":2}
d2 ={'c':3,'d':4}
for k,v in d2.items():
    d1[k]=v
print(d1)'''


"""""using comparasion"""
res={10,11,12,13,14,15,16}
res1={}
res1['even']=[i for i in res if i %2==0]                 
res1['odd']=[i for i in res if i %2!=0]                                  
print(res1)

