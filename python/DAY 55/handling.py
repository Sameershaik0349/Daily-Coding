'''
# w+==>write,read



r+==>write,read
a+==>append,read
rb==>read binary
wb ==>write binary


'''

# w+==>write,read

# with open("file1.txt","w+") as r:
#     r.write("Matter isanything that has mass and takes up space, composed of atoms and molecules. It exists primarily in four states—solid, liquid, gas, and plasma—which differ")
#     r.seek(0)  # for cursor value   ///moving poointer position to  0 so it take index value
#     data =r.read()
#     print(data)


'''seek () -------for chnaging indexing pos

    tell()--------for check cursor position

'''


'''r+  ==>read,write''' # only for existing 
"if we first write in existing its over ride and start form beging with existing file"


'''a+===>append,read
    create new file and append new data
'''
'''with open("filehand1.py","a+") as h:
    data=h.write("123456789")
    h.seek(0)
    data2=h.read()
    print(data2)
'''

# "read binary"
# r=open("image.png","rb")
# data=r.read()
# new =open("image1.png","wb")

# new.write(data)




"write binary"










""
"read ,------3  lines"
"2) readline --------only starting "
""
"3)readline =[] ------in list format data"
"4)writeline -----for store multiple lines of matter"



'''with open ("filehand1.txt","r+") as h:
    data=h.readlines()
    count=0
    for x in data:
        count+=1
print(count)
'''

"words"

# with open("filehand2.txt","r+") as s:
#     data=s.read()
#     data1=data.split()
#     print(len(data1))


"chars"

# with open("filehand2.txt","r+") as j:
#     s=j.read()
#     count=0
#     for i in s:
#         count+=1
# print(count)



"deleting file"

import os

if os.path.exists("file hand.py"):
    os.remove("file hand.py")









