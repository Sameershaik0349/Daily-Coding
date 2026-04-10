# import mysql.connector

# class BankApp:

#     # Constructor (Automatically runs when object is created)
#     def __init__(self):
#         self.db = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Tobi@2704",
#             database="bankdb"
#         )
#         self.cursor = self.db.cursor()
#         print("✅ Connected to Database Successfully!")

#     # Create Account
#     def create_account(self):
#         acc_no = int(input("Enter Account Number: "))
#         name = input("Enter Name: ")
#         balance = float(input("Enter Initial Balance: "))

#         sql = "INSERT INTO accounts (acc_no, name, balance) VALUES (%s, %s, %s)"
#         values = (acc_no, name, balance)

#         try:
#             self.cursor.execute(sql, values)
#             self.db.commit()
#             print("✅ Account Created Successfully!")
#         except:
#             print("❌ Error! Account may already exist.")

#     # Deposit
#     def deposit(self):
#         acc_no = int(input("Enter Account Number: "))
#         amount = float(input("Enter Amount to Deposit: "))

#         self.cursor.execute("SELECT balance FROM accounts WHERE acc_no=%s", (acc_no,))
#         result = self.cursor.fetchone()

#         if result:
#             new_balance = result[0] + amount
#             self.cursor.execute("UPDATE accounts SET balance=%s WHERE acc_no=%s", (new_balance, acc_no))
#             self.db.commit()
#             print("✅ Amount Deposited Successfully!")
#         else:
#             print("❌ Account not found!")

#     # Withdraw
#     def withdraw(self):
#         acc_no = int(input("Enter Account Number: "))
#         amount = float(input("Enter Amount to Withdraw: "))

#         self.cursor.execute("SELECT balance FROM accounts WHERE acc_no=%s", (acc_no,))
#         result = self.cursor.fetchone()

#         if result:
#             if result[0] >= amount:
#                 new_balance = result[0] - amount
#                 self.cursor.execute("UPDATE accounts SET balance=%s WHERE acc_no=%s", (new_balance, acc_no))
#                 self.db.commit()
#                 print("✅ Withdrawal Successful!")
#             else:
#                 print("❌ Insufficient Balance!")
#         else:
#             print("❌ Account not found!")

#     # Check Balance
#     def check_balance(self):
#         acc_no = int(input("Enter Account Number: "))

#         self.cursor.execute("SELECT name, balance FROM accounts WHERE acc_no=%s", (acc_no,))
#         result = self.cursor.fetchone()

#         if result:
#             print(f"👤 Name: {result[0]}")
#             print(f"💰 Balance: {result[1]}")
#         else:
#             print("❌ Account not found!")

#     # Close Connection
#     def close_connection(self):
#         self.db.close()
#         print("🔒 Database connection closed.")


# # ---------------- MAIN PROGRAM ---------------- #

# # Object creation → Constructor is called here
# bank = BankApp()

# while True:
#     print("\n====== BANK MENU ======")
#     print("1. Create Account")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Check Balance")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         bank.create_account()
#     elif choice == '2':
#         bank.deposit()
#     elif choice == '3':
#         bank.withdraw()
#     elif choice == '4':
#         bank.check_balance()
#     elif choice == '5':
#         bank.close_connection()
#         print("👋 Thank you!")
#         break
#     else:
#         print("❌ Invalid Choice!")







# ==================================================PDBC CONNECTION ==============================================

import mysql.connector
import random

con="create database IF  NOT EXISTS linkDB"
sql =mysql.connector.connect(user='root',
                             host='localhost',
                             password='Tobi@2704',
)

cur=sql.cursor()
cur.execute(con)
cur.execute("use linkDB")

sql.commit()

table = """
CREATE TABLE IF NOT EXISTS deatils_bank (
    name VARCHAR(50),
    ifsc_num INT,
    acc_number INT,
    acc_type VARCHAR(20),
    acc_bal FLOAT
)
"""
cur.execute(table)
sql.commit()


table_insert='insert into values'


class sbi():
    def create_acc(self):
        name=input("enter your name: ")
        ifsc_num=random.randint(000000000,999999999)
        acc_number=random.randint(0000000,9999999)
        acc_type=input("enter saving /zero: ").lower()
        while True:
            if acc_type=="saving":
                v1=int(input("you selected saving acc so deposit 1000/- rupees only:-"))
                if v1>=1000:
                    cur.execute(
                            "INSERT INTO deatils_bank (name, ifsc_num, acc_number, acc_type, acc_bal) VALUES (%s, %s, %s, %s, %s)",
                            (name, ifsc_num, acc_number, acc_type, v1))
                    sql.commit()
                    break
                else:
                    print("please deposit 1000/- to countine")
                    
                     

            elif acc_type=="zero":
                v2=int(input("you selected zero acc so deposit 500/- rupees only:-"))

                if v2>=500:
                     cur.execute(
                            "INSERT INTO deatils_bank (name, ifsc_num, acc_number, acc_type, acc_bal) VALUES (%s, %s, %s, %s, %s)",
                            (name, ifsc_num, acc_number, acc_type, v2))
                     sql.commit()
                     break
                else:
                    print("please depoist 500/---")
        print("account created successfully")


    def deposit(self):
        acc_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to deposit: "))

        cur.execute("SELECT acc_bal FROM deatils_bank WHERE acc_number=%s", (acc_number,))
        result = cur.fetchone()

        if result:
            new_balance = result[0] + amount
            cur.execute("UPDATE deatils_bank SET acc_bal=%s WHERE acc_number=%s", (new_balance, acc_number))
            sql.commit()
            print("✅ Amount deposited successfully")
        else:
            print("❌ Account not found")



    def withdraw(self):
        acc_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to withdraw: "))

        cur.execute("SELECT acc_bal FROM deatils_bank WHERE acc_number=%s", (acc_number,))
        result = cur.fetchone()

        if result:
            if result[0] >= amount:
                new_balance = result[0] - amount
                cur.execute("UPDATE deatils_bank SET acc_bal=%s WHERE acc_number=%s", (new_balance, acc_number))
                sql.commit()
                print("✅ Withdrawal successful")
            else:
                print("❌ Insufficient balance")
        else:
            print("❌ Account not found")

    def check_details(self):
        acc_number = int(input("Enter account number: "))

        cur.execute("SELECT name, acc_type, acc_bal FROM deatils_bank WHERE acc_number=%s", (acc_number,))
        result = cur.fetchone()

        if result:
            print("👤 Name:", result[0])
            print("🏦 Account Type:", result[1])
            print("💰 Balance:", result[2])
        else:
            print("❌ Account not found")

obj=sbi()
# obj.create_acc()
# obj.deposit()
# obj.withdraw()
# obj .check_details()


        



