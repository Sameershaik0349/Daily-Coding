import mysql.connector

class BankApp:

    # Constructor (Automatically runs when object is created)
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Tobi@2704",
            database="bankdb"
        )
        self.cursor = self.db.cursor()
        print("✅ Connected to Database Successfully!")

    # Create Account
    def create_account(self):
        acc_no = int(input("Enter Account Number: "))
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))

        sql = "INSERT INTO accounts (acc_no, name, balance) VALUES (%s, %s, %s)"
        values = (acc_no, name, balance)

        try:
            self.cursor.execute(sql, values)
            self.db.commit()
            print("✅ Account Created Successfully!")
        except:
            print("❌ Error! Account may already exist.")

    # Deposit
    def deposit(self):
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount to Deposit: "))

        self.cursor.execute("SELECT balance FROM accounts WHERE acc_no=%s", (acc_no,))
        result = self.cursor.fetchone()

        if result:
            new_balance = result[0] + amount
            self.cursor.execute("UPDATE accounts SET balance=%s WHERE acc_no=%s", (new_balance, acc_no))
            self.db.commit()
            print("✅ Amount Deposited Successfully!")
        else:
            print("❌ Account not found!")

    # Withdraw
    def withdraw(self):
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount to Withdraw: "))

        self.cursor.execute("SELECT balance FROM accounts WHERE acc_no=%s", (acc_no,))
        result = self.cursor.fetchone()

        if result:
            if result[0] >= amount:
                new_balance = result[0] - amount
                self.cursor.execute("UPDATE accounts SET balance=%s WHERE acc_no=%s", (new_balance, acc_no))
                self.db.commit()
                print("✅ Withdrawal Successful!")
            else:
                print("❌ Insufficient Balance!")
        else:
            print("❌ Account not found!")

    # Check Balance
    def check_balance(self):
        acc_no = int(input("Enter Account Number: "))

        self.cursor.execute("SELECT name, balance FROM accounts WHERE acc_no=%s", (acc_no,))
        result = self.cursor.fetchone()

        if result:
            print(f"👤 Name: {result[0]}")
            print(f"💰 Balance: {result[1]}")
        else:
            print("❌ Account not found!")

    # Close Connection
    def close_connection(self):
        self.db.close()
        print("🔒 Database connection closed.")


# ---------------- MAIN PROGRAM ---------------- #

# Object creation → Constructor is called here
bank = BankApp()

while True:
    print("\n====== BANK MENU ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        bank.create_account()
    elif choice == '2':
        bank.deposit()
    elif choice == '3':
        bank.withdraw()
    elif choice == '4':
        bank.check_balance()
    elif choice == '5':
        bank.close_connection()
        print("👋 Thank you!")
        break
    else:
        print("❌ Invalid Choice!")