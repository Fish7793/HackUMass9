import mysql.connector as mysql
import sys
from user import User

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'

class UserDatabase:
    def __init__(self):
        cursor = self.db.cursor()
        try:
            self.db = mysql.connect( ##access db from inside the class
                host = "localhost",
                user = "root",
                passwd = sys.argv[1] if len(sys.argv) > 1 else "",
                database="base"
            )
        except Exception as ex:
            print(ex)
            self.db = mysql.connect( ##access db from inside the class
                host = "localhost",
                user = "root",
                passwd = sys.argv[1] if len(sys.argv) > 1 else "",
            )
            cursor.execute("CREATE DATABASE base")
            cursor.execute("USE base")
        
            cursor.execute("CREATE TABLE users (user_name VARCHAR(255), name VARCHAR(225), password VARCHAR(255), age INT, country VARCHAR(255), email VARCHAR(511), interests VARCHAR(4095), bio VARCHAR(2047), contact VARCHAR(1023), min_age INT, max_age INT)")
            cursor.execute("CREATE TABLE frens (user_name VARCHAR(255), friends VARCHAR(8191))")
        
        cursor.close()

    def close(self):
        self.db.close()

    def add_user(self, user):
        query = ("INSERT INTO users"
                 "(user_name, name, password, age, country, email, interests, bio, contact, min_age, max_age)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = user.get_data_tuple()
        
        ret = self.get_user_by_user_name(user.properties["user_name"])
        if (ret is None):
            cursor = self.db.cursor()
            cursor.execute("USE base")
            cursor.execute(query, values)
            cursor.close()
        else:
            print("User already exists!")

    def delete_user(self, user):  
        query = ("DELETE FROM users WHERE user_name = %s")
        values = (user.properties["user_name"],)
        cursor = self.db.cursor()
        cursor.execute("USE base")
        cursor.execute(query, values)
        cursor.close()

    def get_user_by_user_name(self, user_name):
        query = ("SELECT * FROM users WHERE user_name = %s")
        values = (user_name,)
        cursor = self.db.cursor()
        cursor.execute("USE base")
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        user = User().set_data_from_database(result[0] if len(result) > 0 else None)
        if (user is not None):
            user.properties["password"] = ""
        return user

    def get_users_by_query(self, q):
        '''
        q is a dict = {
            min_age,
            max_age,
            interests,
        }
        '''

        query = ("SELECT * FROM users WHERE age >= %s AND age <= %s")

        values = (q["min_age"], q["max_age"],)
        cursor = self.db.cursor()
        cursor.execute("USE base")
        cursor.execute(query, values)
        results = cursor.fetchall()
        results = [User().set_data_from_database(item) for item in results]
        filtered = list(filter(lambda user: any(y in user.properties["interests"] for y in q["interests"]), results))
        cursor.close()
    
        return filtered
        
    def set_fields(self, user):
        self.delete_user(user)
        self.add_user(user)
    
    def check_user_pass(self, user_name, password):
        query = ("SELECT * FROM users WHERE user_name = %s AND password = %s")
        values = (user_name, password,)
        cursor = self.db.cursor()
        cursor.execute("USE base")
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        return User().set_data_from_database(result[0] if len(result) > 0 else None)

    



# database = UserDatabase()
# bob = User().set_properties({
#     "name":"Bob",
#     "user_name":"Hekrrmann",
#     "age":21,
#     "email":"bob@hackumass.com",
#     "password":"12345",
#     "country":"US",
#     "interests":{ "Hacking", "Coding" },
#     "bio":"howdy ;)",
#     "contact": { "hekk9982" },
# })

# steve = User().set_properties({
#     "name":"Steve",
#     "user_name":"CS_GOD",
#     "age":17,
#     "email":"stev@edgelord.com",
#     "password":"54321",
#     "country":"US",
#     "interests":{ "Hacking", "Knitting" },
#     "bio":"guh XC",
#     "contact": { "guh29492", "guh#29382" }
# })

# database.add_user(bob)
# database.add_user(steve)
# print(database.retrieve_user_by_user_name("Hekrrmann"))
# bob.properties["age"] = 99
# database.set_fields(bob)
# print(database.retrieve_user_by_user_name("Hekrrmann"))

# print(database.retrieve_user_by_user_name("CS_GOD"))
# print(database.retrieve_users_by_query({
#     "min_age":0,
#     "max_age":99,
#     "interests": {"Hacking"}
# }))
# database.delete_user(bob)
# database.delete_user(steve)
# print(database.retrieve_user_by_user_name("Hekrrmann"))
# database.close()