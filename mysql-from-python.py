import os
import pymysql
if os.path.exists("env.py"):
    import env

# Get username from the env.py file
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
# password not used in this file now, can be deleted, just example

# Connect to database
connection = pymysql.connect(host="localhost",
                             user=username,
                             password='',
                             db="Chinook")
try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ["fred", "Fred"]
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(
            format_strings), list_of_names)
        connection.commit()
finally:
    # Close connection
    connection.close()
