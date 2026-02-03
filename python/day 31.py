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







""
k = "reverse each word in a sentence"

words = k.split()   
result = []         

for w in words:
    rev = ""
    for ch in w:
        rev = ch + rev 
    result.append(rev)   

print(result)

# print(d)


