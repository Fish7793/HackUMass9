import sys
import mysql.connector as mysql


class ChatDatabase:
    def __init__(self):
        try:
            self.db = mysql.connect( ##access db from inside the class
                host = "localhost",
                user = "root",
                passwd = sys.argv[1] if len(sys.argv) > 1 else "",
                database="chat"
            )
        except Exception as ex:
            print(ex)
            self.db = mysql.connect( ##access db from inside the class
                host = "localhost",
                user = "root",
                passwd = sys.argv[1] if len(sys.argv) > 1 else "",
            )

            cursor = self.db.cursor()
            cursor.execute("CREATE DATABASE chat")
            cursor.execute("USE chat")
            cursor.execute("CREATE TABLE chat (user1 VARCHAR(255), user2 VARCHAR(225), chat VARCHAR(8192))")
            cursor.close()
    
    def close(self):
        self.db.close()

    # we need a way to try get chat matching user1 and user2 from the database

    # we need a way to store that chat in a datastructure