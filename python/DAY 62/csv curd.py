# csv

"update"

import csv
t=[]
with open('employee1.csv','r')as n:
    r=csv.reader(n)
    for x in r:
        if x[0]=='101':
            x[2]='200000'
        t.append(x)
print(t)

with open('employee1.csv','w', newline='') as c:
    a=csv.writer(c)
    a.writerows(t)




# import csv
# with open('employee1.csv','w',newline="") as p:
#     wr=csv.writer(p)
#     wr.writerow(["empid","emp_name","emp_salary"])
#     mul=([101,"sam",1000],
#          [102,'sai',2000],
#          [103,'kumar',3000])
#     wr.writerows(mul)

