import mysql.connector as mysql
import sys
from user import User

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'

class UserDatabase:
    def __init__(self):
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
            cursor = self.db.cursor()

            cursor.execute("CREATE DATABASE base")
            cursor.execute("USE base")
        
            cursor.execute("CREATE TABLE users (user_name VARCHAR(255), name VARCHAR(225), password VARCHAR(255), age INT, country VARCHAR(255), email VARCHAR(511), interests VARCHAR(4095), bio VARCHAR(2047), contact VARCHAR(1023), min_age INT, max_age INT)")
            cursor.execute("CREATE TABLE frens (user_name VARCHAR(255), friends VARCHAR(8191))")
        
            cursor.close()

#sadilfjaseo

    def close(self):
        self.db.close()

    def add_user(self, user, frens = []):
        query1 = ("INSERT INTO users"
                 "(user_name, name, password, age, country, email, interests, bio, contact, min_age, max_age)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values1 = user.get_data_tuple()
        
        query2 = ("INSERT INTO frens"
                 "(user_name, friends)"
                 "VALUES (%s, %s)")
        values2 = (user.properties["user_name"], self.lst_to_friend_str(frens),)
        
        
        ret = self.get_user_by_user_name(user.properties["user_name"])
        if (ret is None):
            cursor = self.db.cursor()
            cursor.execute("USE base")
            cursor.execute(query1, values1)
            cursor.execute(query2, values2)
            cursor.close()
        else:
            print("User already exists!")

        return self

    def delete_user(self, user):  
        query = ("DELETE FROM users WHERE user_name = %s")
        query2 = ("DELETE FROM frens WHERE user_name = %s")
        values = (user.properties["user_name"],)
        cursor = self.db.cursor()
        cursor.execute("USE base")
        cursor.execute(query, values)
        cursor.execute(query2, values)
        cursor.close()

        return self

    def get_user_by_user_name(self, user_name):
        query = ("SELECT * FROM users WHERE user_name = %s")
        values = (user_name,)
        cursor = self.db.cursor()
        cursor.execute("USE base")
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        user = User().set_from_database(result[0] if len(result) > 0 else None)
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
        results = [User().set_from_database(item) for item in results]
        filtered = list(filter(lambda user: any(y in user.properties["interests"] for y in q["interests"]), results))
        cursor.close()
    
        return filtered
        
    def set_fields(self, user):
        self.delete_user(user)
        frens = self.get_friends(user.properties["user_name"])
        self.add_user(user, frens)
        return self
    
    def check_user_pass(self, user_name, password):
        query = ("SELECT * FROM users WHERE user_name = %s AND password = %s")
        values = (user_name, password,)
        cursor = self.db.cursor()
        cursor.execute("USE base")
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        return User().set_from_database(result[0] if len(result) > 0 else None)

    def add_friend(self, user_name, other_name):
        lst = self.get_friends(user_name)
        lst.append(other_name)

        query = ("UPDATE frens SET friends = %s WHERE user_name = %s")
        values = (self.lst_to_friend_str(lst), user_name)
        
        cursor = self.db.cursor()
        cursor.execute("USE base")
        cursor.execute(query, values)
        cursor.close()
        
        return self

    def friend_str_to_lst(self, str):
        return str.split(",")
    
    def lst_to_friend_str(self, lst):
        return ",".join(list(lst))

    def get_friends(self, user_name):
        query = ("SELECT friends FROM frens WHERE user_name = %s")
        values = (user_name, )
        cursor = self.db.cursor()
        cursor.execute("USE base")
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        t = self.friend_str_to_lst((result[0][0] if len(result) > 0 else ""))
        return list(filter(lambda x: x != '' and x is not None, t))

    def remove_friend(self, user_name, other_name):
        lst = self.get_friends(user_name)
        if (other_name in lst):
            lst.remove(other_name)

        query = ("UPDATE frens SET friends = %s WHERE user_name = %s")
        values = (self.lst_to_friend_str(lst), user_name)
        
        cursor = self.db.cursor()
        cursor.execute("USE base")
        cursor.execute(query, values)
        cursor.close()
        return self

    def check_if_mutual(self, user_name, other_name):
        return user_name in self.get_friends(other_name) and other_name in self.get_friends(user_name)

    



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
# print(database.get_friends("Hekrrmann"))
# database.add_friend("Hekrrmann", "CS_GOD")
# database.add_friend("CS_GOD", "Hekrrmann")
# print(database.check_if_mutual("CS_GOD", "Hekrrmann"))

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
# print(database.get_user_by_user_name("Hekrrmann"))
# print(database.get_friends("Hekrrmann"))

# database.close()