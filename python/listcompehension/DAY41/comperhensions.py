"28/02/26"
"dic comperhension"


""

# res1={}
# for x in range(1,10):
#     res1[x]=x**2
# print(res1)

# res={x:x**2 for x in range(1,10)}
# print(res)

# res={'a':10,'b':20}
# r={}
# for k,v in res.items():
#     r[v]=k
# print(r)

# res={v:k for k,v in res.items()}
# print(res)

" "



# res={x:{'sqare':x**2,'cube':x**3} for x in range(1,3)}
# print(res)


""

res={chr(x):x for x in range(97,123) if x %2==0}
print(res)

res1=["cat","dog","bat"]
res={x:x[::-1] for x in res1}
print(res)

