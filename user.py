class User:
    def __init__(self):
        self.user_name = ""
        self.name = ""
        self.password = ""
        self.age = 0
        self.country = ""
        self.email = ""
        self.interests = set()

    def set_data_from_database(self, tuple):
        if (tuple == None):
            return None
        self.user_name = tuple[0]
        self.name = tuple[1]
        self.password = tuple[2]
        self.age = tuple[3]
        self.country = tuple[4]
        self.email = tuple[5]
        self.interests = set(tuple[6].split(","))
        return self

    def get_data_tuple(self):
        return (self.user_name, self.name, self.password, self.age, self.country, self.email, ",".join(tuple(self.interests)),)
        
