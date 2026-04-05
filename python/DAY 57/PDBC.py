"pdbc"
# PYTHON DATABASE Connection

import mysql.connector

con="Create Database pdbc"
sql=mysql.connector.connect(user='root',
                  host='localhost',
                  password='Tobi@2704')
cursor=sql.cursor()# method
cursor.execute(con)

sql.close()