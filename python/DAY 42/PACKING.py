"Packing"


"one varible contains more than one value"
# *rules
"we surely give varible for every varible////if not it gives error"

'''a =[10,20,30,40] #packing
n,m,i,l=a     #[10,20,30,40]
print(m)

'''
"unpacking"

'''a=[10,20,30,40,50]
d,*b,c=a
print(d)
print(b)
print(c)
'''

"functions  x  unpacking"

def demo(a,b):
    print(a+b)
s=10,20
demo(*s)