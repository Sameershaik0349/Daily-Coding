# import mysql.connector
# import random

# db="create database IF NOT EXISTS bank_pdbc"
# sql=mysql.connector.connect(
#     user="root",
#     host="localhost",
#     password="Tobi@2704"
# )

# con=sql.cursor()
# con.execute(db)
# con.execute("use bank_pdbc")

# table_sql="create table IF NOT EXISTS bank_details (name varchar(20),acc_no int,acc_type varchar(20),deposit Float)"

# con.execute(table_sql)

# sql.commit()


# class sbi():
#     def create_acc(self):
#         name=input("enter your name :")
#         acc_no=random.randint(000000000,999999999)
#         acc_type=input('enter your acc_type: saving/zeroo')
#         deposit=int(input("enter you amount"))

#         insert_details="""INSERT INTO bank_details (acc_no, name, acc_type,deposit)VALUES(%s,%s,%s,%s)"""
#         val = (acc_no, name, acc_type, deposit)
#         con.execute(insert_details,val)
#         sql.commit()

# obj=sbi()
# obj.create_acc()




# # import mysql.connector
# # import random

# # # DB Connection
# # sql = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     password="Tobi@2704"
# # )

# # con = sql.cursor()

# # # Create DB
# # con.execute("CREATE DATABASE IF NOT EXISTS bank_pdb")

# # # Use DB
# # con.execute("USE bank_pdb")

# # # Create Table (FIXED)
# # table_sql = """
# # CREATE TABLE IF NOT EXISTS bank_details (
# #     acc_no INT PRIMARY KEY,
# #     name VARCHAR(20),
# #     acc_type VARCHAR(20),
# #     balance FLOAT
# # )
# # """
# # con.execute(table_sql)

# # sql.commit()


# # class SBI:

# #     def create_acc(self):
# #         name = input("Enter your name: ")
# #         acc_no = random.randint(100000000, 999999999)
# #         acc_type = input("Enter account type (saving/zero): ")
# #         deposit = int(input("Enter amount: "))

# #         # CORRECT INSERT
# #         insert_details = """
# #         INSERT INTO bank_details (acc_no, name, acc_type, balance)
# #         VALUES (%s, %s, %s, %s)
# #         """

# #         val = (acc_no, name, acc_type, deposit)

# #         con.execute(insert_details, val)
# #         sql.commit()
# #         print("Account Number:", acc_no)




# # # Run
# # obj = SBI()
# # obj.create_acc()
 
