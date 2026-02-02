"string methods"
# p ="Python Devo"
# f=''
# for i in p:
#     if i.isupper():
#         f+="_"+i
#     elif i.islower():
#         f+=i
# print(f)


p ="@python@devo"
res=""
for i in p:
    if i.isalpha():
        res+=i
print(res)