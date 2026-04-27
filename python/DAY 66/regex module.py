# # regex
# '''methods

# match     ==> only starting ch check
# full match ===> total
# find all ==>charcters finding    ,list daatype[]
# finditer =>charcters finding     ,index and charcter 
# search  ==>chr search            ,index ,chr
# sub ==>  chr replace
# subn  ==>nu.of replace count
# slipt ==>sentence split            ,[]
# '''
# # meta characters

# '''
# .   ==>total charcters execpt new line
# +  ==>1 and more than one  printing
# *  ==> 0 and more  than 0
# ?  ==> 0 or 1 
# ^ == starts with
# $ ==>endsiwth
# []  =>exactly char
# {1}  =>no.of charcter
# {1,3} ==>between charcter






# classes 

# 1) \d  ==> 0-9
# \D  ==>except digits
# \ w ==> a-z A-Z 0-9  _
# \W ==> special charcters
# \s ==> spaces
# \S ==>non white spaces
# '''



# import re

# s='''ejadsb j bv s d j bs j ah dbja hbdj chsbj chba sjdb2 345678910293278yuhjSBNAJHXvCHSAB DHW67327QUW H@#%$'''
# # r =re.findall(r'\d+',s)
# # print(r)

# b='''ejadsb j bv s d j bs j ah dbja hbdj chsbj chba sjdb2
#  345678910293278yuhjSBNAJHXvCHSAB DHW67327QUW H@#%$'''

# # r =re.findall(r'\w+',b)
# # print(r)

# import re

# 'mobile'

# '6-9 ==> 09 9'

# a = ''''ejadsb j bv s d j bs j ah dbja hbdj chsbj chba sjdb2 +91 6789098766 yuhjSBNA+91 7032175956JHXvCHSAB DHW67327QUW H@#%$'''
# d=re.findall(r'[+]91 [6-9]{1}[0-9]{9}',a)
# print(d)



# import re

# pat="sksameer46644@gmail.com"

# d=re.fullmatch(r'\w+@gmail.com',pat)

# if d:
#     print("val")
# else:
#     print("invalid")

import re
pat='TS09AB1234'
d=re.fullmatch('[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}[0-9]{4}',pat)
if d:
    print("val")
else:
    print("invalid")