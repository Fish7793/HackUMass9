import mysql.connector as mysql
import sys

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'

class Database:
    def __init__(self):
    
        self.db = mysql.connect( ##access db from inside the class
            host = "localhost",
            user = "root",
            passwd = sys.argv[1] if len(sys.argv) > 1 else ""
        )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE friendDatabase (user_name VARCHAR(255), name VARCHAR(225), password VARCHAR(255), age (int), country VARCHAR(255), email VARCHAR(500), interests VARCHAR(500))")

        print(self.db)

    def close(self):
        self.db.close()

    def add_user():
        add_user = ("INSERT INTO friendDatabase"
                   "(user_name, name, password, age, country, email, interests)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")


    def delete_user():  
        delete_user = ("DELETE FROM friendDatabase")

    def retrieve_user():
        retrieve_user = ("SELECT * FROM friendDatabase WHERE age LIKE '% %' ")
        

database = Database()

database.close()

##add to the database 

##database class 
##
