import os
import pymysql
if os.path.exists("env.py"):
    import env

# Get username from the env.py file
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD') #this is not used in this file now, can be deleted, just example

# Connect to database
connection = pymysql.connect(host="localhost",
                             user=username, #here we are using the username set on line 7 above
                             password='',
                             db="Chinook")
try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close connection
    connection.close()
