"pdbc"
# PYTHON DATABASE Connection

'creating table'
'''import mysql.connector

con="Create Database pdbc"
sql=mysql.connector.connect(user='root',
                  host='localhost',
                  password='Tobi@2704')
cursor=sql.cursor()# method
cursor.execute(con)

sql.close()'''


# import mysql.connector

# con1="create table(std_id int,std_name varchar(20),std_age int)"

# sql=mysql.connector.connect(user='root',
#                             host='localhost',
#                             database='pdbc',
#                             password='Tobi@2704')
# cur=sql.cursor()
# cur.execute(con1)
# sql.commit()
# sql.close()


'''

import mysql.connector

con1 = "CREATE TABLE student (std_id INT, std_name VARCHAR(20), std_age INT)"

sql = mysql.connector.connect(
    user='root',
    host='localhost',
    database='pdbc',
    password='Tobi@2704'
)

cur = sql.cursor()
cur.execute(con1)

sql.commit()   # ✅ important

sql.close()'''




'''import mysql.connector

con1 = "insert into student(101,'sameer',15)"

sql = mysql.connector.connect(
    user='root',
    host='localhost',
    database='pdbc',
    password='Tobi@2704'
)

cur = sql.cursor()
cur.execute(con1)

sql.commit()   

sql.close()'''





'''import mysql.connector

sql = mysql.connector.connect(
    user='root',
    host='localhost',
    database='pdbc',
    password='Tobi@2704'
)

cur = sql.cursor()

query = "INSERT INTO student VALUES (%s, %s, %s)"
values = (101, 'sameer', 15)

cur.execute(query, values)

sql.commit()   # ✅ important

sql.close()'''


'''
import mysql.connector

con1 = "INSERT INTO student VALUES (102, 'saheb', 21)"

sql = mysql.connector.connect(
    user='root',
    host='localhost',
    database='pdbc',
    password='Tobi@2704'
)

cur = sql.cursor()
cur.execute(con1)

sql.commit()   

sql.close()'''



# "usnng loop for inserting mul records "


# import mysql.connector



# user=int(input("how many records you want to insert"))
# sql=mysql.connector.connect(
#     user='root',
#     host='localhost',
#     database='pdbc',
#     password='Tobi@2704'
# )

# cur = sql.cursor()
# for i in range(1,user+1):
#     id=(int(input("enter your id")))
#     name=(input("enter your name"))
#     age=(input("enter your age"))

    
#     con="insert into student values (%s,%s,%s)"
#     values=(id,name,age)
#     cur.execute(con,values)

#     sql.commit()   
#     print(f'{i}',"records inserted")

# sql.close()




'''import mysql.connector



user=int(input("how many records you want to insert"))
sql=mysql.connector.connect(
    user='root',
    host='localhost',
    database='pdbc',
    password='Tobi@2704'
)

cur = sql.cursor()
while user:
    id=(int(input("enter your id")))
    name=(input("enter your name"))
    age=(input("enter your age"))

    
    con="insert into student values (%s,%s,%s)"
    values=(id,name,age)
    cur.execute(con,values)

    sql.commit()   
    print("records inserted")
    user-=1



sql.close()'''
# ===================updating===================================


import mysql.connector

con="update student set std_name='h' where std_id = 110"
sql=mysql.connector.connect(user='root',
                            host='localhost',
                            database='pdbc',
                            password='Tobi@2704')

cur=sql.cursor()
cur.execute(con)

sql.commit()

sql.close()

