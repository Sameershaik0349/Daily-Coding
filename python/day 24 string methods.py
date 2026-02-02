"iterating by len"
# p = "wewq"
# for i in range (len(p)):
#     print(p[i])

"upper"
# p = 'python'
# c=0
# up=""
# for x in p:
#     if ord(x) >=97 and ord(x) <=122:
#         c = ord(x) - 32
#         up += chr(c)
# print(up)
"lower"
# p ="PYTHON"
# for i in p:
#     if ord(i) >=65 and ord(i)<=91:
#         d = ord(i) +32
#         print(chr(d))
"swap case"

# f = "pYtHoN"
# out=""
# for i in f:
#     if ord(i) >=97 and ord(i)<=122:
#         d = ord(i) -32 
#         out+=chr(d)
#     elif ord (i) >=65 and ord(i)<=91:
#         c =ord(i) +32
#         out+=chr(c)
# print(out)

"finding a length without using len"

p ='sameer saheb'
count =0
for i in p:
   if i in p:
      count+=1
print(count)

# n = 5
# line = '*' * 1
# for i in range(n+1):
#     print(line)

# "convert string to list"           #its do like this ['P', 'y', 'r', 'a', 'm', 'i', 'd', ' ', '(', 'C', 'e', 'n', 't', 'e', 'r', 'e', 'd', ')']
# p  ="Pyramid (Centered)"
# d =list(p)
# print(d)

# ""

# p="Pyramid (Centered)"         # its do like this                 ['Pyramid', '(Centered)']
# d =p.split('i')                     # if we give any lterr in box        ['Pyram', 'd (Centered)']
# print(d)


# g = "sameer saheb"
# d =g.split()
# for i in d:
#     print(g.split())

# "is upper or is lower" # alternate method for assic values
# g = "SaMeeR sAhEb"
# for i in g:
#     if i.isupper():
#         print(i)
#     # elif i.islower():
#     #     print(i)
