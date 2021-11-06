import sys
import mysql.connector as mysql


class ChatDatabase:
    def __init__(self, user):
        self.user = user
        try:
            self.db = mysql.connect( ##access db from inside the class
                host = "localhost",
                user = "root",
                passwd = sys.argv[1] if len(sys.argv) > 1 else "",
                database=user.properties["user_name"]
            )
        except Exception as ex:
            print(ex)
            self.db = mysql.connect( ##access db from inside the class
                host = "localhost",
                user = "root",
                passwd = sys.argv[1] if len(sys.argv) > 1 else "",
            )

            cursor = self.db.cursor()
            cursor.execute("CREATE DATABASE {}".format(user.properties["user_name"]))
            cursor.execute("USE {}".format(user.properties["user_name"]))
            cursor.close()
    
    def close(self):
        self.db.close()

    def try_start_chat(self, other_user):
        cursor = self.db.cursor()
        cursor.execute("USE {}".format(self.user.properties["user_name"]))
        cursor.execute("CREATE TABLE {} (user_name VARCHAR(255), date DATE, chat VARCHAR(1024))".format(other_user.properties["user_name"]))
        cursor.close()
        pass

    def try_add_to_chat(self, other_user):
        cursor = self.db.cursor()
        cursor.execute("USE {}".format(self.user.properties["user_name"]))

        pass

    def try_get_chat(self, other_user):
        cursor = self.db.cursor()
        cursor.execute("USE {}".format(self.user.properties["user_name"]))

        pass

    # we need a way to try get chat matching user1 and user2 from the database

    # we need a way to store that chat in a datastructure