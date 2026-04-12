import csv
# student=open("student.csv",'w',newline="")
# filed_name=csv.writer(student)

# filed_name.writerow(['std_id','std_name','std_age'])


# filed_name.writerow([101,"same",21])



# emp=open("employe.csv",'w',newline="")

# emp0=csv.writer(emp)
# emp0.writerow(['emp_id','emp_name','emp_sal'])

# emp0.writerow([101,"sucks",200000])




# with open("employee.csv",'w',newline="") as n:
#     wr=csv.writer(n)
#     wr.writerow(['emp_id','emp_name','emp_sal'])

#     mul=([101,'sameer',1000000],
#          [102,'sucks',200000])
    
#     wr.writerow([mul])






# with open("employee1.csv",'w',newline="") as n:
#     wr=csv.writer(n)
#     wr.writerow(["emp_id",'emp_name','emp_sal'])
    
#     b=int(input("number of employee records"))

#     for x in range(1,b+1):
#         emp_id=int(input('enter employe id'))
#         emp_name=input("enter employe name")
#         emp_sal=float(input('enter emp_sal'))

#         wr.writerow([emp_id,emp_name,emp_sal])
#         print(f"{x} record inserted")




'read'



# with open('employee1.csv','r') as p:
#     # r=csv.reader(p)
#     r=csv.DictReader(p) #---for dict format
#     for x in r:
#         print(x)
                       




"write using dict"

# with open('employee1.csv','a',newline="") as n:
#     f=(['emp_id','emp_name','emp_sal'])
#     wr=csv.DictWriter(n,fieldnames=f)
#     wr.writerow({
#         'emp_id':101,
#         'emp_name':'sameer',
#         'emp_sal':11111111
#     })



