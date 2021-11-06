class User:
    def __init__(self):
        self.properties = dict()
        self.properties["user_name"] = ""
        self.properties["name"] = ""
        self.properties["password"] = ""
        self.properties["age"] = 0
        self.properties["country"] = ""
        self.properties["email"] = ""
        self.properties["interests"] = set()
        self.properties["bio"] = ""
        self.properties["contact"] = set()

    def set_properties(self, p):
        self.properties = p
        return self

    def set_data_from_database(self, tuple):
        if (tuple == None):
            return None
        self.properties["user_name"] = tuple[0]
        self.properties["name"] = tuple[1]
        self.properties["password"] = tuple[2]
        self.properties["age"] = tuple[3]
        self.properties["country"] = tuple[4]
        self.properties["email"] = tuple[5]
        self.properties["interests"] = set(tuple[6].split(","))
        self.properties["bio"] = tuple[7]
        self.properties["contact"] = set(tuple[8].split(","))
        return self

    def get_data_tuple(self):
        return (self.properties["user_name"], 
                self.properties["name"], 
                self.properties["password"], 
                self.properties["age"], 
                self.properties["country"], 
                self.properties["email"], 
                ",".join(tuple(self.properties["interests"])),
                self.properties["bio"],
                ",".join(tuple(self.properties["contact"])))

    def __str__(self) -> str:
        t = ""
        for k, v in self.properties.items():
            t += "[{} : {}], ".format(k, v)

        return t
        
