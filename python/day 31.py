# "sring problems"
# vow="aeiou"
# k = "replace"
# tem=""
# for i in k:
#     if i in vow:
#         tem+="*"
#     else:
#         tem+=i
# print(tem)

# "anagram"
# s1 = "listen"
# s2 = "silent"

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")



# s1 = 'race'
# s2 = "care"
# if sorted(s1) == sorted(s2):
#     print("its anagram")
# else:
#     print("not a angram")


# "using dict"
# k = "anagram"
# res={}
# for i in k:
#     if i not in res:
#         res[i]=1
#     else:
#         res[i]+=1
# print(res)







"reverse a string and store in list"
# k = "reverse each word in a sentence"

# words = k.split()   
# result = []         

# for w in words:
#     rev = ""
#     for ch in w:
#         rev = ch + rev 
#     result.append(rev)   

# print(result)

# print(d)



# k = "sameersaheb"
# h={}
# for i in k:
#     if i not in h:
#         h[i]=1
#     else:
#         h[i]+=1  #h[i] = h[i] + 1
# print(h)

# h ="characters are the digits"
# d = h.split()
# # char=""
# res=0
# for i in d:
#     char=""
#     if len(i)>res:
#         res=len(i)
#         char=i
# print(res)
# print(char)


"Reverse a string without using slicing or reverse()."

# y ="sameeer"
# g=""
# for i in y:
#     if y not in g:
#         g=i+g
# print(g)

"Check whether a string is a palindrome"
# y = "madam"
# g=""
# for i in y:
#     g=i+g
# if y == g:
#     print("its palindrom")
# else:
#     print("not a palindrom")

"Count the frequency of each character in a string."

# b ="banana"
# d={}
# for i in b:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)


"Find the first non-repeating character in a string"

# g = "sameer"
# for i in range(len(g)):
#     count=0
#     for y in range(len(g)):
#         if g[i]==g[y]:
#             count+=1
#     if count==1:
#         print('its a first nonreparting values',g[i])
#         break
""
# g = "banana"
# d ={}
# for i in g:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]=d[i]+1
# for i in g:
#     if d[i]==1:
#         print("first reapting value is ",i)
#         break




"Remove duplicate characters from a string."

# s ="banana"
# res=""
# for i in s:
#     if i not in res:
#         res+=i
# print(res)
    
"Find the maximum occurring character in a string."

# s = "banana"
# res={}
# for i in s:
#     if i in res:
#         res[i]+=1
#     else:
#         res[i]=1
# max_value=""
# max_count=0
# for i in s:
#     if res[i]>max_count:
#         max_count=res[i]
#         max_value=i
# print("max value",max_value)
# print("count",max_count)

"Count the number of vowels and consonants in a string."

# name = "sameer"
# vow ="AEIOU".lower()
# count_vow=0
# count_consonants=0
# for i in name:
#     if i in vow:
#         count_vow+=1
    
#     else:
#         count_consonants+=1
# print(" its consotnat",count_consonants)
# print("its vowel",count_vow)

""
# name = "sameer saheb"

# vow= "AEIOU".lower()

# count_vow=0
# count_constant=0
# for i in  name:
#     if i.isalpha():
#         if i in vow:
#             count_vow+=1
#         else:
#             count_constant+=1
#     print("count of constant",count_constant,i)
#     print("count of vow",count_vow,i)

"Reverse each word in a string."
 
# s ="Reverse each word in a string."
# d = s.split()
# k=[]
# for i in d:
#     rev=""
#     for y in i:
#         rev= y+rev
#     k.append(rev)
# print(k)
# print("".join(k))

# g ="123"
# num=0
# for i in g:
# #     num = num * 10 +(ord(i)-ord("0"))
# # print(num)
#     print(ord(i))


f = "pyhton devlopper"
d = f.capitalize()
print(d)