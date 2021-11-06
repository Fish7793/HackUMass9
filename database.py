import mysql.connector as mysql
import sys

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = sys.argv[1] if len(sys.argv) > 1 else ""
)

print(db) # it will print a connection object if everything is fine