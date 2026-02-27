
# res=[x for x  in range(10,20)if all(x%y!=0 for y in range(2,x))]
# print (res)



j=11
res=[x for x in range(1,j+1)if j%x==0]
if len(res)==2:
    print("its a prime")
else:
    print("not a prime")